from http.client import responses

import requests
from config.config import BASE_URL, API_KEY

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)

def create_user(payload):
    return requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

def update_user(user_id, payload):
    return requests.put(f"{BASE_URL}/users/{user_id}", json=payload, headers=HEADERS)

def delete_user(user_id):
    return requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
