from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database
from models.models import User

client = TestClient(app)


def test_login_success():
    response = client.post("/users/login", data={"username": "meghana", "password": "new_password"})

    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)


def test_add_user_success():
    user_request_data = {
        "user_name": "prakash",
        "email": "sanjanavonteri@gmail.com",
        "password": "prakash1234",
        "address": "Test Address",
        "phone": "1234567890",
        "created_by": 0
    }

    response = client.post("/users/register_user", json=user_request_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User added successfully."
    user = session.query(User).filter_by(user_name=user_request_data["user_name"]).first()
    assert user is not None
    assert user.user_name == user_request_data["user_name"]
    assert user.email == user_request_data["email"]


# def test_add_user_invalid_data():
#     invalid_user_request_data = {
#         "user_name": "test_user",
#         "email": "invalid_email",
#         "password": "test_password",
#         "address": "Test Address",
#         "phone": "123",
#         "created_by": 0
#     }
#
#     response = client.post("/users/register_user", json=invalid_user_request_data)
#
#     assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtZWdoYW5hIiwiZXhwIjoxNjkwNDI4OTMzfQ.j5kX36mTxgVXfttnuHUNPVdmMGpJ55g6jXRpzy54q2o"


def test_read_user_success():
    user_name = "meghana"

    response = client.get(f"/users/{user_name}", headers={"Authorization": f"Bearer {auth_token}"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["user_name"] == user_name


def test_read_user_unauthorised():
    unauthorised_user_name = "bhavana"

    response = client.get(f"/users/{unauthorised_user_name}")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_read_all_users_success():
    response = client.get('/users', headers={"Authorization": f"Bearer {auth_token}"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Users retrieved successfully."


def test_update_user_success():
    user_name = "sanjana_reddy"

    new_user_data = {
        "user_name": "sanjana_reddy",
        "email": "sanjanavonteri@gmail.com",
        "password": "Sanjana1234",
        "address": "this is Updated Address",
        "phone": "9391030701"
    }

    response = client.put(
        f"/users/update_user/{user_name}",
        json=new_user_data,
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User updated successfully"
    updated_user = session.query(User).filter_by(phone=new_user_data["phone"]).first()
    assert updated_user is not None
