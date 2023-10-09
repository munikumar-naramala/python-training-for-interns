import unittest
from unittest.mock import Mock, patch
from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


@patch('db.database.Database.get_db_session')
@patch('db.database.Database.get_db_connection')
def test_assign_delivery_partner_success(mock_get_db_connection, mock_get_db_session):
    order_id = "9f927643-db06-4bc5-b001-4854593fc1fd"

    mock_db_connection = Mock()
    mock_get_db_connection.return_value = mock_db_connection
    mock_db_connection.assign_delivery_partner.return_value = {'message': 'Delivery partner assigned successfully!'}

    response = client.post(f"/delivery/assign_partner/{order_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "message" in response.json()
    assert response.json()["message"] == "Delivery partner assigned successfully!"


@patch('db.database.Database.get_db_session')
@patch('db.database.Database.get_db_connection')
def test_add_delivery_partner_success(mock_get_db_connection, mock_get_db_session):
    delivery_partner_request_data = {
        "contact_info": "venkatvonteri@gmail.com",
        "status": 0
    }

    mock_db_connection = Mock()
    mock_get_db_connection.return_value = mock_db_connection

    delivery_partner = MockDeliveryPartner()
    delivery_partner.id = "some_random_id"
    mock_db_connection.add_delivery_partner.return_value = delivery_partner

    response = client.post("/delivery/register_delivery_partner", json=delivery_partner_request_data)

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert "id" in response.json()["data"]
    assert response.json()["message"] == "Delivery Partner added successfully."
    assert response.json()["error"] is False


@patch('db.database.Database.get_db_session')
@patch('db.database.Database.get_db_connection')
def test_read_all_delivery_partners_success(mock_get_db_connection, mock_get_db_session):
    delivery_partner1 = MockDeliveryPartner()
    delivery_partner2 = MockDeliveryPartner()

    mock_db_connection = Mock()
    mock_get_db_connection.return_value = mock_db_connection
    mock_db_connection.read_all_delivery_partners.return_value = [delivery_partner1, delivery_partner2]

    response = client.get("/delivery/")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert response.json()["message"] == "DPs retrieved successfully."
    assert response.json()["error"] is False


class MockDeliveryPartner:
    def __init__(self):
        self.id = None


if __name__ == "__main__":
    unittest.main()
