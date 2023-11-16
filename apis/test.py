from petstore.user.user import User
from petstore.pet.pet import Pet, SoldPets, list_sold_pets


print(">>>>>>>> Create User >>>>>>>>")

user = User(username="test_user", password="password", email="test@test.com",
            firstName="Test", lastName="User", phone="1234567890", userStatus=0)
response = user.create_user()
print(f"Create user response: {response.json()}")
assert response.status_code == 200

print(">>>>>>>> Get created user info >>>>>>>>")

response = user.get_user()
assert response.status_code == 200
assert response.json()["username"] == "test_user"
assert response.json()["firstName"] == "Test"
assert response.json()["lastName"] == "User"

print(f"User info: {response.json()}")


print(">>>>>>>> Create sold pets >>>>>>>>")
pet_a = Pet(id=0, category={"id": 0, "name": "TestJordi"}, name="TestJordi", photoUrls=["string"], tags=[{"id": 0, "name": "TestJordi"}], status="sold")
pet_b = Pet(id=0, category={"id": 0, "name": "TestJordi"}, name="TestJordi", photoUrls=["string"], tags=[{"id": 0, "name": "TestJordi"}], status="sold")
response = pet_a.create_pet()
assert response.status_code == 200
print(f"Create pet response: {response.json()}")
response = pet_b.create_pet()
assert response.status_code == 200
print(f"Create pet response: {response.json()}")

print(">>>>>>>> List sold pets >>>>>>>>")
sold_pets = list_sold_pets()

for pet in sold_pets.items():
    print(f"Sold pet: {pet}")

print(">>>>>>>> Count pet repeated names >>>>>>>>")

sold_pets_object = SoldPets(sold_pets)
pet_repeated_names = sold_pets_object.count_repeated_pet_names()

print(f"Count of pet names: {pet_repeated_names}")




