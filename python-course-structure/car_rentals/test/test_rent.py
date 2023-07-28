from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_add_rent_success():
    rent_request_data = {
        "user_id": "93126e27-819f-4953-a384-3ef57f803299",
        "vehicle_id": "8de55152-076a-4238-965d-6bb821356f30",
        "duration": 2,
        "start_date": "2023-07-28T04:22:08.075Z"
    }

    response = client.post("/rent/add_rent", json=rent_request_data)

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert "rent_id" in response.json()["data"]
    assert response.json()["message"] == "Rent added successfully."
    assert response.json()["error"] is False


def test_read_rent_success():
    rent_id = "269a0af1-ac4c-4ef2-bac0-219eb506d918"

    response = client.get(f"/rent/{rent_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert response.json()["message"] == "Rent retrieved successfully"


def test_read_rent_not_found():
    rent_id = "8de55152-6bb821356f30"

    response = client.get(f"/rent/{rent_id}")

    assert response.json()["message"] == "Rent Not found"
    assert response.json()["error"] is False


def test_read_all_rents_success():
    response = client.get("/rent/")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert response.json()["message"] == "Rents retrieved successfully."
    assert response.json()["error"] is False
