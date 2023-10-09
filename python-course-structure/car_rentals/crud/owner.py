from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.request import OwnerRequest, Token, OwnerUpdateRequest
from schemas.response import response
from models.models import Owner
from db.database import Database
from sqlalchemy import and_, desc
import uuid
import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
import bcrypt
from static.send_mail import send_email

router = APIRouter(
    prefix="/owner",
    tags=["Owner"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/owner/login")

SECRET_KEY = '867b6d70449e152a6d3363c1c6f35430bca7359ffd6128504e8f6710c48614af'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_owner(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        owner = payload.get("sub")
        if owner is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return owner
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post("/login", response_model=Token)
def owner_login(form_data: OAuth2PasswordRequestForm = Depends()):
    owner_name = form_data.username
    owner_password_hash = form_data.password

    session = database.get_db_session(engine)
    owner = session.query(Owner).filter_by(owner_name=owner_name).first()
    if owner is None or not bcrypt.checkpw(owner_password_hash.encode('utf-8'),
                                           owner.owner_password_hash.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    session.close()

    data = {"sub": owner.owner_name}
    token = create_access_token(data=data)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register_owner", response_description="Add a owner")
async def add_owner(owner_req: OwnerRequest):
    new_owner = Owner()
    new_owner.owner_id = str(uuid.uuid4())
    new_owner.owner_name = owner_req.owner_name
    new_owner.owner_email = owner_req.owner_email
    new_owner.owner_password_hash = bcrypt.hashpw(owner_req.owner_password_hash.encode('utf-8'), bcrypt.gensalt())
    new_owner.owner_address = owner_req.owner_address
    new_owner.owner_phone = owner_req.owner_phone
    session = database.get_db_session(engine)
    session.add(new_owner)
    session.flush()
    session.refresh(new_owner, attribute_names=['owner_id'])
    data = {"owner_id": new_owner.owner_id}
    try:
        session.commit()
        subject = "Registration Successful"
        message = f"Hello {new_owner.owner_name},\n\nYour registration to the vehicle rental app is successful."
        session.close()
        send_email(subject, message, new_owner.owner_email)
    except Exception as exception:
        print('exception is: ', exception)
    finally:
        session.close()
    return response(data, 200, "Owner added successfully.", False)


@router.post("/forgot_password")
async def owner_forgot_password(owner_email: str, current_owner: str = Depends(get_current_owner)):
    session = database.get_db_session(engine)
    owner = session.query(Owner).filter_by(owner_email=owner_email).first()
    if owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")

    new_password = "new_password"

    owner.owner_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    session.commit()
    session.add(owner)

    subject = "Password Reset"
    message = f"Hello {owner.owner_name},\n\nYour new password is: {new_password}"
    session.close()
    send_email(subject, message, owner.owner_email)

    return response(None, 200, "Password reset email sent successfully.", False)


@router.get("/{owner_name}")
async def read_owner(owner_name: str, current_owner: str = Depends(get_current_owner)):
    session = database.get_db_session(engine)
    response_message = "Owner retrieved successfully"
    data = None
    try:
        data = session.query(Owner).filter(
            and_(Owner.owner_name == owner_name)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Owner Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_owners(current_owner: str = Depends(get_current_owner)):
    session = database.get_db_session(engine)
    data = session.query(Owner).order_by(
        desc(Owner.created_at)).all()
    return response(data, 200, "Owners retrieved successfully.", False)


@router.put("/update_owner/{owner_id}")
async def update_owner(owner_update_req: OwnerUpdateRequest, owner_id: str,
                       current_owner: str = Depends(get_current_owner)):
    session = database.get_db_session(engine)
    try:
        is_owner_updated = session.query(Owner).filter(Owner.owner_id == owner_id).update({
            Owner.owner_name: owner_update_req.owner_name,
            Owner.owner_email: owner_update_req.owner_email,
            Owner.owner_password_hash: bcrypt.hashpw(owner_update_req.owner_password_hash.encode('utf-8'),
                                                     bcrypt.gensalt()),
            Owner.owner_address: owner_update_req.owner_address,
            Owner.owner_phone: owner_update_req.owner_phone
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Owner updated successfully"
        response_code = 200
        error = False
        if is_owner_updated == 1:
            data = session.query(Owner).filter(
                Owner.owner_id == owner_id).one()
            return response(data, response_code, response_msg, error)

    except Exception as ex:
        print("Error : ", ex)


@router.post("/logout")
def logout(current_owner: str = Depends(get_current_owner)):
    return response({}, 200, "Owner logged out successfully.", False)
