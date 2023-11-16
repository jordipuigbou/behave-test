import requests
from ..config.api import URL, API_VERSION
from os import path



PET_ENDPOINT="pet"

def get_pet_by_status(status):
    response = requests.get(path.join(URL,API_VERSION,PET_ENDPOINT,"findByStatus"), params={"status": status})
    return response

def list_sold_pets():
    response = get_pet_by_status("sold")
    pet_tuple = {}
    for pet in response.json():
        try:
            pet_tuple[pet["id"]] = pet["name"]
        except KeyError:
            print(f"Pet {pet['id']} does not have a name")
    return pet_tuple

class SoldPets:
    def __init__(self, sold_pets):
        self.sold_pets = sold_pets

    def count_repeated_pet_names(self):
        pet_names = []
        for pet in self.sold_pets:
            pet_names.append(self.sold_pets[pet])
        return {pet_name: pet_names.count(pet_name) for pet_name in pet_names}

class Pet:
    def __init__(self, id, category, name, photoUrls, tags, status):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status

    def __str__(self):
        return f"Pet: {self.name}"

    def __repr__(self):
        return f"Pet: {self.name}"

    def create_pet(self):
        payload = {
            "id": self.id,
            "category": self.category,
            "name": self.name,
            "photoUrls": self.photoUrls,
            "tags": self.tags,
            "status": self.status
        }
        response = requests.post(path.join(URL,API_VERSION,PET_ENDPOINT), json=payload)
        return response

    def get_pet(self):
        response = requests.get(path.join(URL,API_VERSION,PET_ENDPOINT,self.id))
        return response



    def update_pet(self):
        payload = {
            "id": self.id,
            "category": self.category,
            "name": self.name,
            "photoUrls": self.photoUrls,
            "tags": self.tags,
            "status": self.status
        }
        response = requests.put(path.join(URL,API_VERSION,PET_ENDPOINT), json=payload)
        return response

    def delete_pet(self):
        response = requests.delete(path.join(URL,API_VERSION,PET_ENDPOINT,self.id))

