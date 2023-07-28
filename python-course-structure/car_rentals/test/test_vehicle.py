from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database
from models.models import Vehicle

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_add_vehicle_success():
    vehicle_request_data = {
        "owner_id": "56f93117-f22c-47f1-8209-7183c403bd3e",
        "registration_number": "45879tweiruhkljf",
        "type": "Car",
        "brand": "Volkswagen",
        "model": "GT TSI Polo",
        "year": 2019,
        "color": "white",
        "amount_per_hour": 400,
        "is_available": 1
    }

    response = client.post("/vehicle/add_vehicle", json=vehicle_request_data)

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert "vehicle_id" in response.json()["data"]
    assert response.json()["message"] == "Vehicle added successfully."
    assert response.json()["error"] is False


def test_read_vehicle_success():
    vehicle_id = "8de55152-076a-4238-965d-6bb821356f30"

    response = client.get(f"/vehicle/{vehicle_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert response.json()["message"] == "Vehicle retrieved successfully"


def test_read_menu_not_found():
    vehicle_id = "8de55152-6bb821356f30"

    response = client.get(f"/vehicle/{vehicle_id}")

    assert response.json()["message"] == "Vehicle Not found"
    assert response.json()["error"] is False


def test_read_all_vehicles_success():
    response = client.get("/vehicle/")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert response.json()["message"] == "Vehicles retrieved successfully."
    assert response.json()["error"] is False


def test_update_vehicle_success():
    vehicle_id = "8de55152-076a-4238-965d-6bb821356f30"

    new_vehicle_data = {
        "registration_number": "1002",
        "type": "Car",
        "brand": "Volkswagen",
        "model": "GT TSI Polo",
        "year": "2019",
        "color": "white",
        "amount_per_hour": "400",
        "is_available": 1
    }

    response = client.put(f"/vehicle/update_vehicle/{vehicle_id}", json=new_vehicle_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Vehicle details updated successfully"
    updated_vehicle = session.query(Vehicle).filter_by(
        registration_number=new_vehicle_data["registration_number"]).first()
    assert updated_vehicle is not None
