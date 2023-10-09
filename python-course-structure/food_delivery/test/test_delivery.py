from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_assign_delivery_partner_success():
    order_id = "9f927643-db06-4bc5-b001-4854593fc1fd"

    response = client.post(f"/delivery/assign_partner/{order_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "message" in response.json()
    assert response.json()["message"] == "Delivery partner assigned successfully!"


def test_add_delivery_partner_success():
    delivery_partner_request_data = {
        "contact_info": "sanjanavonteri@gmail.com",
        "status": 0
    }

    response = client.post("/delivery/register_delivery_partner", json=delivery_partner_request_data)

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert "id" in response.json()["data"]
    assert response.json()["message"] == "Delivery Partner added successfully."
    assert response.json()["error"] is False


def test_read_all_delivery_partners_success():
    response = client.get("/delivery/")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0
    assert response.json()["message"] == "DPs retrieved successfully."
    assert response.json()["error"] is False
