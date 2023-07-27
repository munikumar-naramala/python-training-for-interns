from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_calculate_order_total_success():
    user_id = "ec107624-a419-48a6-b8a4-72dc2cfe1e62"
    order_id = "dc984321-76a3-4623-b14d-0daf6e69491a"

    response = client.get(f"/get_amount/{user_id}/{order_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "total_amount" in response.json()


def test_calculate_order_total_order_not_found():
    user_id = "ec107624-a419-48a6-b8a4-72dc2cfe1e62"
    order_id = "dc98434d-0daf6e69491a"

    response = client.get(f"/get_amount/{user_id}/{order_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
