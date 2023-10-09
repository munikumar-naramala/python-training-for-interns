from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.request import UserRequest, Token, UserUpdateRequest
from schemas.response import response
from models.models import User
from db.database import Database
from sqlalchemy import and_, desc
import uuid
import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
import bcrypt
from static.send_mail import send_email

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

SECRET_KEY = '867b6d70449e152a6d3363c1c6f35430bca7359ffd6128504e8f6710c48614af'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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
def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password_hash = form_data.password

    session = database.get_db_session(engine)
    user = session.query(User).filter_by(username=username).first()
    if user is None or not bcrypt.checkpw(password_hash.encode('utf-8'), user.password_hash.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    session.close()

    data = {"sub": user.username}
    token = create_access_token(data=data)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register_user", response_description="Add a user")
async def add_user(user_req: UserRequest):
    new_user = User()
    new_user.user_id = str(uuid.uuid4())
    new_user.username = user_req.username
    new_user.email = user_req.email
    new_user.password_hash = bcrypt.hashpw(user_req.password_hash.encode('utf-8'), bcrypt.gensalt())
    new_user.address = user_req.address
    new_user.phone = user_req.phone
    session = database.get_db_session(engine)
    session.add(new_user)
    session.flush()
    session.refresh(new_user, attribute_names=['user_id'])
    data = {"user_id": new_user.user_id}
    try:
        session.commit()
        subject = "Registration Successful"
        message = f"Hello {new_user.username},\n\nYour registration to the vehicle rental app is successful."
        session.close()
        send_email(subject, message, new_user.email)
    except Exception as exception:
        print('exception is: ', exception)
    finally:
        session.close()
    return response(data, 200, "User added successfully.", False)


@router.post("/forgot_password")
async def user_forgot_password(email: str, current_user: str = Depends(get_current_user)):
    session = database.get_db_session(engine)
    user = session.query(User).filter_by(email=email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    new_password = "new_password"

    user.password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    session.commit()
    session.add(user)

    subject = "Password Reset"
    message = f"Hello {user.username},\n\nYour new password is: {new_password}"
    session.close()
    send_email(subject, message, user.email)

    return response(None, 200, "Password reset email sent successfully.", False)


@router.get("/{username}")
async def read_user(username: str, current_user: str = Depends(get_current_user)):
    session = database.get_db_session(engine)
    response_message = "User retrieved successfully"
    data = None
    try:
        data = session.query(User).filter(
            and_(User.username == username)).one()
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


@router.put("/update_user/{user_id}")
async def update_user(user_update_req: UserUpdateRequest, user_id: str,
                      current_user: str = Depends(get_current_user)):
    session = database.get_db_session(engine)
    try:
        is_user_updated = session.query(User).filter(User.user_id == user_id).update({
            User.username: user_update_req.username,
            User.email: user_update_req.email,
            User.password_hash: bcrypt.hashpw(user_update_req.password_hash.encode('utf-8'), bcrypt.gensalt()),
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
                User.user_id == user_id).one()
            return response(data, response_code, response_msg, error)

    except Exception as ex:
        print("Error : ", ex)


@router.post("/logout")
def logout(current_user: str = Depends(get_current_user)):
    return response({}, 200, "User logged out successfully.", False)
