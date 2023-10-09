from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_add_order_success():
    order_data = {
        "user_id": "ec107624-a419-48a6-b8a4-72dc2cfe1e62",
        "restaurant_id": "a62212c2-8122-4b78-8ca3-76511cfd7b16",
        "order_status": "Pending",
        "amount": 0,
        "payment_status": "Pending"
    }

    response = client.post("/orders/add_order", json=order_data)

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert "order_id" in response.json()["data"]
    assert response.json()["message"] == "Order added successfully."
    assert response.json()["error"] is False


def test_read_order_existing_order():
    sample_order_id = "7f324296-580c-48ce-8849-64a2b33f50b9"

    response = client.get(f"/orders/{sample_order_id}")

    assert response.status_code == 200

    # assert response.json()["data"]["order_id"] == "sample_order_id"
    # assert response.json()["data"]["restaurant_id"] == "restaurant_id_1"
    # assert response.json()["message"] == "Order retrieved successfully"
    # assert response.json()["error"] == False


def test_read_order_not_found():
    order_id = "158f-4f01-a92d-d1d7039cda8f"

    response = client.get(f"/orders/{order_id}")

    assert response.json()["message"] == "Order Not found"


def test_read_all_orders_success():
    response = client.get("/orders/")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0
    assert response.json()["message"] == "Orders retrieved successfully."
    assert response.json()["error"] is False
