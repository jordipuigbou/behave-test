import requests
from ..config.api import URL, API_VERSION
from os import path

USER_ENDPOINT="user"


class User:
    def __init__(self, username, password, email, firstName, lastName, phone, userStatus):
        self.username = username
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.userStatus = userStatus


    def __str__(self):
        return f"User: {self.username}"

    def __repr__(self):
        return f"User: {self.username}"

    def create_user(self):
        payload = {
            "id": 0,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.userStatus
        }
        # join paths URL, API_VERSION, USER_ENDPOINT
        request_path = path.join(URL,API_VERSION,USER_ENDPOINT)

        response = requests.post(request_path, json=payload)
        return response

    def get_user(self):
        response = requests.get(path.join(URL,API_VERSION,USER_ENDPOINT,self.username))
        return response

