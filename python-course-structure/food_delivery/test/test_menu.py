from fastapi.testclient import TestClient
from fastapi import status
from main import app
from db.database import Database

database = Database()
engine = database.get_db_connection()

session = database.get_db_session(engine)

client = TestClient(app)


def test_add_menu_success():
    menu_request_data = {
        "restaurant_id": "a9032ee0-7ab6-47d5-9fb7-a11a972b0a04",
        "food_name": "Naatu Kodi Pulusu",
        "cuisine": "South Indian",
        "amount": 300
    }

    response = client.post("/menu/add_menu", json=menu_request_data)

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert "menu_id" in response.json()["data"]
    assert response.json()["message"] == "Menu added successfully."
    assert response.json()["error"] is False


def test_read_menu_success():
    menu_id = "f5bef898-7d1c-4f2f-9236-78660120fa13"

    response = client.get(f"/menu/{menu_id}")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    # assert response.json()["message"] == "Menu retrieved successfully"


def test_read_menu_not_found():
    menu_id = "7d71897ef"

    response = client.get(f"/menu/{menu_id}")

    assert response.json()["message"] == "Menu Not found"
    assert response.json()["error"] is False


def test_read_all_menus_success():
    response = client.get("/menu/")

    assert response.status_code == status.HTTP_200_OK
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0
    assert response.json()["message"] == "Menus retrieved successfully."
    assert response.json()["error"] is False


def test_search_menu_success():
    query = "a62212c2-8122-4b78-8ca3-76511cfd7b16"

    response = client.get(f"/menu/menu/search?query={query}")

    assert response.status_code == status.HTTP_200_OK
    assert "results" in response.json()
    assert len(response.json()["results"]) > 0
