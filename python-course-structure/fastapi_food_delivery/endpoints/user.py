from fastapi import APIRouter
from models.request import UserRequest, UserUpdateRequest
from models.response import Response
from models.models import User
from db.database import Database
from sqlalchemy import and_, desc
from fastapi.exceptions import HTTPException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
from jose import jwt
from pydantic import BaseModel
from datetime import datetime, timedelta


def send_email(subject: str, message: str, recipient: str):
    sender_email = "reddy.sanjana2002@gmail.com"
    sender_password = "riaatcbhizndhcxk"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))


router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


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
    except Exception as exception:
        print('exception is: ', exception)
    finally:
        session.close()
    return Response(data, 200, "User added successfully.", False)


class Token(BaseModel):
    access_token: str
    token_type: str


SECRET_KEY = '867b6d70449e152a6d3363c1c6f35430bca7359ffd6128504e8f6710c48614af'
ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


@router.post("/login")
def login(user_name: str, password: str):
    session = database.get_db_session(engine)
    user = session.query(User).filter_by(user_name=user_name).first()
    if user is None or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    session.flush()
    session.commit()
    session.close()

    data = {
        'info': 'secret information',
        'from': 'GFG'
    }
    token = create_access_token(data=data)
    return {'token': token, 'login status: ': 'success'}


@router.post("/forgot_password")
async def forgot_password(email: str):
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

    return Response(None, 200, "Password reset email sent successfully.", False)


@router.post("/logout")
def logout():
    return Response({}, 200, "User logged out successfully.", False)


@router.put("/update_user/{user_name}")
async def update_menu(user_update_req: UserUpdateRequest, user_name: str):
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
            return Response(data, response_code, response_msg, error)

    except Exception as ex:
        print("Error : ", ex)


@router.get("/{user_name}")
async def read_user(user_name: str):
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
    return Response(data, 200, response_message, error)


@router.get("/")
async def read_all_users():
    session = database.get_db_session(engine)
    data = session.query(User).order_by(
        desc(User.created_at)).all()
    return Response(data, 200, "Users retrieved successfully.", False)
