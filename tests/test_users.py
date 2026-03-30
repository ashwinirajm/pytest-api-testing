import pytest

from data.test_data import create_user_payload, update_user_payload
from utils.api_client import *

def test_get_user(user_id):
    response = get_user(user_id)

    data = response.json()
    print("Response:", data)

    assert response.status_code == 200
    assert data["data"]["id"] == user_id

def test_create_user():
    response = create_user(create_user_payload)

    print("Response:", response.json())

    assert response.status_code == 201
    assert response.json()["name"] == create_user_payload["name"]

def test_update_user():
    response = update_user(2, update_user_payload)

    print("Response:", response.json())

    assert response.status_code == 200

def test_delete_user():
    response = delete_user(2)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    assert response.status_code == 204


def test_get_invalid_user():
    response = get_user(999)

    print("Response:", response.json())

    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_multiple_users(user_id):
    response = get_user(user_id)

    data = response.json()

    print("Response:", response.json())

    assert response.status_code == 200
    assert "data" in data
    assert data["data"]["id"] == user_id


def test_response_structure():
    response = get_user(2)

    data = response.json()

    assert "data" in data
    assert "id" in data["data"]
    assert isinstance(data["data"]["id"], int)