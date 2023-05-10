# This script uses the `requests` library to send HTTP requests to the containerized user profile application at the URL `http://localhost:8000/api/users`. It tests the creation, retrieval, updating, and deletion of a user, and prints out a message indicating whether each test was successful or not. Note that the specific URLs and data used in this script will depend on the API endpoints and data model of your user profile application.


import requests

# Define the URL of the containerized application url = "http://localhost:8000/api/users"

# Define the test data
data = {
    "name": "Austin Goodin",
    "email": "test@example.com",
    "age": 31,
    "gender": "male"
}

# Test the creation of a new user
response = requests.post(url, json=data) if response.status_code == 201:
    print("User created successfully")
else:
    print("Error creating user")

# Test the retrieval of the newly created user response = requests.get(url + "/1") if response.status_code == 200:
    user = response.json()
    if user["name"] == data["name"] and user["email"] == data["email"]:
        print("User retrieved successfully")
    else:
        print("Retrieved user data does not match test data")
else:
    print("Error retrieving user")

# Test the updating of the newly created user new_data = {
    "name": "Jane Doe",
    "email": "janedoe@example.com",
    "age": 32,
    "gender": "female"
}
response = requests.put(url + "/1", json=new_data) if response.status_code == 200:
    user = response.json()
    if user["name"] == new_data["name"] and user["email"] == new_data["email"]:
        print("User updated successfully")
    else:
        print("Updated user data does not match test data")
else:
    print("Error updating user")

# Test the deletion of the newly created user response = requests.delete(url + "/1") if response.status_code == 204:
    print("User deleted successfully")
else:
    print("Error deleting user")
