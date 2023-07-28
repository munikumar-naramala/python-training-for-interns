from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_calculate_order_total_success():
    rent_id = "ae7a9f59-45d0-45ea-a3e1-195909cd149f"

    response = client.get(f"/get_total_amount/{rent_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "total_amount" in response.json()
