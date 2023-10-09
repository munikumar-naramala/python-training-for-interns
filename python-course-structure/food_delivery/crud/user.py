from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.request import UserRequest, UserUpdateRequest
from schemas.response import response
from models.models import User
from db.database import Database
from sqlalchemy import and_, desc
import uuid
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from static.send_mail import send_email
from schemas.request import Token

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

SECRET_KEY = '867b6d70449e152a6d3363c1c6f35430bca7359ffd6128504e8f6710c48614af'
ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = payload.get("sub")
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
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
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_name = form_data.username
    password = form_data.password

    session = database.get_db_session(engine)
    user = session.query(User).filter_by(user_name=user_name).first()
    if user is None or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    session.close()

    data = {"sub": user.user_name}
    token = create_access_token(data=data)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register_user", response_description="Add a user")
async def add_user(user_req: UserRequest):
    new_user = User()
    new_user.user_id = str(uuid.uuid4())
    new_user.user_name = user_req.user_name
    new_user.email = user_req.email
    new_user.password = user_req.password
    new_user.address = user_req.address
    new_user.phone = user_req.phone
    new_user.created_by = user_req.created_by
    session = database.get_db_session(engine)
    session.add(new_user)

    session.flush()
    session.refresh(new_user, attribute_names=['user_id'])
    data = {"user_id": new_user.user_id}
    try:
        session.commit()
        subject = "Registration Successful"
        message = f"Hello {new_user.user_name},\n\nYour registration to the food delivery app is successful."
        session.close()
        send_email(subject, message, new_user.email)
    except Exception as exception:
        print('exception is: ', exception)
    finally:
        session.close()
    return response(data, 200, "User added successfully.", False)


@router.post("/forgot_password")
async def forgot_password(email: str, current_user: str = Depends(get_current_user)):
    session = database.get_db_session(engine)
    user = session.query(User).filter_by(email=email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    new_password = "new_password"

    user.password = new_password
    session.commit()
    session.add(user)

    subject = "Password Reset"
    message = f"Hello {user.user_name},\n\nYour new password is: {new_password}"
    session.close()
    send_email(subject, message, user.email)

    return response(None, 200, "Password reset email sent successfully.", False)


@router.get("/{user_name}")
async def read_user(user_name: str, current_user: str = Depends(get_current_user)):
    session = database.get_db_session(engine)
    response_message = "User retrieved successfully"
    data = None
    try:
        data = session.query(User).filter(
            and_(User.user_name == user_name)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "User Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/")
async def read_all_users(current_user: str = Depends(get_current_user)):
    session = database.get_db_session(engine)
    data = session.query(User).order_by(
        desc(User.created_at)).all()
    return response(data, 200, "Users retrieved successfully.", False)


@router.put("/update_user/{user_name}")
async def update_menu(user_update_req: UserUpdateRequest, user_name: str,
                      current_user: str = Depends(get_current_user)):
    session = database.get_db_session(engine)
    try:
        is_user_updated = session.query(User).filter(User.user_name == user_name).update({
            User.user_name: user_update_req.user_name,
            User.email: user_update_req.email,
            User.password: user_update_req.password,
            User.address: user_update_req.address,
            User.phone: user_update_req.phone
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "User updated successfully"
        response_code = 200
        error = False
        if is_user_updated == 1:
            data = session.query(User).filter(
                User.user_name == user_name).one()
            return response(data, response_code, response_msg, error)

    except Exception as ex:
        print("Error : ", ex)


@router.post("/logout")
def logout(current_user: str = Depends(get_current_user)):
    return response({}, 200, "User logged out successfully.", False)
