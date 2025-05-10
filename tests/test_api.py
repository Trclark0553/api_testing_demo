import requests
import allure
import pytest

# Base URL for the API under test (JSONPlaceholder demo API)
BASE_URL = "https://jsonplaceholder.typicode.com"

# Allure Metadata:
# @allure.feature: Categorizes the test under a specific functional area (for organized reporting).
# @allure.severity: Assigns the business or technical impact of the test case.
# 
# Purpose: 
# These tags improve test report readability and help stakeholders quickly filter 
# critical tests in the Allure report. This is especially valuable for identifying 
# high-risk failures during release readiness assessments.

@allure.feature("Posts API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_post():
    """
    Test: Retrieve a single post by ID
    Purpose: Validate the API returns correct post data for a valid ID (positive test)
    Expected Result: HTTP 200 OK, and response contains expected post fields
    """
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "Expected status code 200 for existing post"

    data = response.json()
    assert data["id"] == 1, "Returned post ID does not match requested ID"
    assert "title" in data, "Title field is missing in response payload"
    assert "body" in data, "Body field is missing in response payload"

@allure.feature("Posts API")
@allure.severity(allure.severity_level.NORMAL)
def test_post_not_found():
    """
    Test: Attempt to retrieve a non-existent post
    Purpose: Validate the API correctly handles invalid post requests (negative test)
    Expected Result: HTTP 404 Not Found or empty response with HTTP 200 (JSONPlaceholder returns 200)
    """
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404, "Expected HTTP 404 for non-existent post"

    #Confirm response body empty
    data = response.json() if response.content else {}
    assert data == {}, "Expected empty JSON response for non-existent post"

@allure.feature("Posts API")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_post():
    """
    Test: Create a new post via POST
    Purpose: Validate that the API successfully accepts new post data (positive test)
    Expected Result: HTTP 201 Created, and response includes submitted data
    """
    payload = {
        "title": "Automation Test Post",
        "body": "This is a test created by automated API testing.",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    # Attach raw response for debugging, for detailed response data in report
    allure.attach(
        response.text,
        name="API Response",
        attachment_type=allure.attachment_type.JSON,
    )

    assert response.status_code == 201, "Expected status code 201 for successful post creation"

    data = response.json()
    # Validate submitted data is echoed back
    assert data["title"] == payload["title"], "Returned title does not match submitted data"
    assert data["body"] == payload["body"], "Returned body does not match submitted data"
    assert data["userId"] == payload["userId"], "Returned userId does not match submitted data"
    assert "id" in data, "Response missing generated post ID"

@allure.feature("Posts API")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.skip(reason="Skipping test for demonstration purposes")
def test_update_post():
    """Skipped Test: Placeholder for future PUT request test"""
    pass
    # This test is skipped to demonstrate my knowledge of the use of pytest.mark.skip

@allure.feature("Posts API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(reason="Known issue: API does not support DELETE verification")
def test_delete_post():
    """Expected Failure Test: Attempt to delete a post (simulated)"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    # JSONPlaceholder API does not actually delete, but we can check status
    assert response.status_code == 200, #This will fail intentionally to show the xfail behavior