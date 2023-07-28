from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database
from models.models import Owner

client = TestClient(app)


def test_login_success():
    response = client.post("/owner/login", data={"username": "meghana", "password": "meghana"})

    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)


def test_add_owner_success():
    owner_request_data = {
        "owner_name": "prakash",
        "email": "sanjanavonteri@gmail.com",
        "password_hash": "prakash",
        "address": "Test Address",
        "phone": "1234567890"
    }

    response = client.post("/user/register_user", json=user_request_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User added successfully."
    user = session.query(User).filter_by(username=user_request_data["username"]).first()
    assert user is not None
    assert user.username == user_request_data["username"]
    assert user.email == user_request_data["email"]


auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtZWdoYW5hIiwiZXhwIjoxNjkwNTE1ODEwfQ.sDs5UF90G-t1JLIvpUWqXKgrGDaMipIFZWBh7oky9dw"


def test_read_user_success():
    username = "prakash"

    response = client.get(f"/user/{username}", headers={"Authorization": f"Bearer {auth_token}"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["username"] == username


def test_read_all_users_success():
    response = client.get('/user', headers={"Authorization": f"Bearer {auth_token}"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Users retrieved successfully."


def test_update_user_success():
    user_id = "fea1f4c9-dc97-4dd5-8928-78ba7ed260ca"

    new_user_data = {
        "user_name": "prakash",
        "email": "sanjanavonteri@gmail.com",
        "password_hash": "prakash",
        "address": "this is Updated Address",
        "phone": "9391030701"
    }


    response = client.put(
        f"/user/update_user/{user_id}",
        json=new_user_data,
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User updated successfully"
    updated_user = session.query(User).filter_by(phone=new_user_data["phone"]).first()
    assert updated_user is not None
