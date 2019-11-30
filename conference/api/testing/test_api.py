import json
import requests
import os

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'
DATA_END_POINT = 'http://localhost:8000/api/events/public/'

data = {
    "username": "mahi",
    "password": "mahi@123"
}

r = requests.post(AUTH_ENDPOINT, data=data)

token = r.json()['token']

print(token)
headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + token
}

events = requests.get(DATA_END_POINT, headers=headers)

print(events.request.headers)
print(events.json())
