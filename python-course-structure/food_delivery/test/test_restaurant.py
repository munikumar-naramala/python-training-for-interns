from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database
from models.models import Restaurant

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_add_restaurant_success():
    restaurant_request_data = {
        "restaurant_name": "Military Hotel",
        "address": "hotel address",
        "phone": "1234567890",
        "email": "codenowyes@gmail.com",
        "opening_hours": "10:00 AM - 8:00 PM",
        "description": "authentic telangana andhra",
        "rating": 4,
        "created_by": 0
    }

    response = client.post("/restaurants/register_restaurant", json=restaurant_request_data)

    assert response.status_code == status.HTTP_200_OK

    restaurant = session.query(Restaurant).filter_by(restaurant_name=restaurant_request_data["restaurant_name"]).first()
    assert restaurant is not None
    assert restaurant.restaurant_name == restaurant_request_data["restaurant_name"]
    assert restaurant.email == restaurant_request_data["email"]


def test_login_success():
    email = "sanjanavonteri@gmail.com"

    response = client.post("/restaurants/login?email=" + email)

    assert response.status_code == 200
    assert "token" in response.json()
    assert "login status: " in response.json()
    assert response.json()["login status: "] == "success"


def test_update_restaurant_success():
    restaurant_id = "a62212c2-8122-4b78-8ca3-76511cfd7b16"
    update_data = {
        "restaurant_name": "Naatu",
        "description": "Updated again restaurant description.",
        "rating": 4
    }

    response = client.put(f"/restaurants/update_restaurant/{restaurant_id}", json=update_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Restaurant details updated successfully"
    restaurant = session.query(Restaurant).filter_by(restaurant_name=update_data["restaurant_name"]).first()

    assert restaurant is not None
