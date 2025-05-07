import requests

# Base URL for th e API under test (uses Reqres demo API)
BASE_URL = "https://reqres.in/api"

def test_get_user():
    """
    Test: Retrieve a single user by their ID
    Purpose: Validate the API returns correct user data for given valid ID (positive test)
    Expected: HTTP 200 OK, and response contains expected user fields
    """
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.satus_code == 200, "Expected status code 200 for existing user"

    data = response.json()
    assert data["data"]["id"] == 2, "Returned user ID does not match requested ID"
    assert "email" in data["data"], "Email field is empty in the returned response payload"

def test_user_not_found():
    """
    Test: Attempt to retrieve a user that doesn't exist"
    Purpose: Validate the API correctly handles non-existant user requests (negative test)
    Expected: HTTP 404 Not Found 
    """
    response = requests.get(f"{BASE_URL}/users/999") #Reqres public API does not have user with ID 999
    assert response.status_code == 404, "Expected 404 for non-existent user ID"
