from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_place_order_success():
    order_item_request_data = {
        "order_id": "158838c2-fd9f-4f01-a92d-d1d7039cda8f",
        "user_id": "012c84ba-4745-44a9-8314-34b9410388df",
        "menu_ids": ["6ded6cda-bae0-4473-b900-86ecac76aa08", "fbee69e-9107-4900-ab57-d33940000a62"],
        "restaurant_id": "c8a92e71-9333-4a28-a368-063f0c79eab0",
        "food_names": ["Palak Chole", "kulcha paratha"],
        "amounts": ["250", "150"],
        "quantities": ["2", "1"]
    }

    response = client.post("/order_items/place_order/", json=order_item_request_data)

    assert "message" in response.json()
    assert response.json()["message"] == "Order placed successfully!"


def test_read_orders_success():
    order_items_id = "9e2c9c69-8295-4eff-b450-4d948c632944"

    response = client.get(f"/order_items/{order_items_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert response.json()["message"] == "Order Items  retrieved successfully"


def test_read_orders_not_found():
    order_items_id = "9e2c9c69-850-4d948c632944"

    response = client.get(f"/order_items/{order_items_id}")

    assert response.json()["message"] == "Order item Not found"
    assert response.json()["error"] is False
