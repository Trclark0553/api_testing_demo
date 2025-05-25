import requests
import allure
import pytest
from pydantic import BaseModel, ValidationError
from jsonschema import validate, ValidationError

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
@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_post(post_id):
    """
    Test: Retrieve a post by ID
    Purpose: Validate the API returns correct post data for multiple valid IDs (positive test)
    Expected Result: HTTP 200 OK, and response contains expected post fields
    """
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200, f"Expected status code 200 for post ID {post_id}"

    data = response.json()
    assert data["id"] == post_id, "Returned post ID does not match requested ID"
    assert "title" in data, "Title field is missing in response payload"
    assert "body" in data, "Body field is missing in response payload"

@allure.feature("Posts API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("post_id", [0, -1, 99999])
def test_post_not_found(post_id):
    """
    Test: Attempt to retrieve non-existent posts
    Purpose: Validate the API correctly handles invalid post requests (negative test)
    Expected Result: HTTP 404 Not Found or empty response with HTTP 200 (JSONPlaceholder returns 200)
    """
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 404, f"Expected HTTP 404 for non-existent post ID {post_id}"

    #Confirm response body empty
    data = response.json() if response.content else {}
    assert data == {}, "Expected empty JSON response for non-existent post"

@allure.feature("Posts API")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("name, job", [
    ("Jake Fernanded", "Software Engineer"),
    ("Travis Clark", "QA Tester"),
    ("Karl Storz", "CEO")
])
def test_create_post(name, job):
    """
    Test: Create a new post via POST with various payloads
    Purpose: Validate that the API successfully accepts new post data (positive test)
    Expected Result: HTTP 201 Created, and response includes submitted data
    """
    payload = {"name": name, "job": job}
    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201, "Expected status code 201 for successful post creation"

    if response.status_code != 201:
        # Attach the response content to Allure report for debugging
        allure.attach(
            response.text,
            name="Response Content",
            attachment_type=allure.attachment_type.TEXT,
        )

    data = response.json()
    # Validate submitted data is echoed back
    assert data["name"] == name, "Returned name does not match submitted name"
    assert data["job"] == job, "Returned job does not match submitted job"
    assert "id" in data, "ID field is missing in response payload"

#Define the exepected JSON schema for a post object
post_schema = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}

@allure.feature("Posts API")
@allure.severity(allure.severity_level.NORMAL)
def test_get_post_jsonschema_validation():
    """
    Test: Validate the JSON schema of the retrieved post data
    Purpose: Ensure the API response adheres to the expected schema (defined above) (positive test)
    Expected Result: HTTP 200 OK, and response matches JSON schema
    """
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "Expected status code 200 for existing post"

    data = response.json()
    try:
        validate(instance=data, schema=post_schema)  # Validate agaist JSON schema
    except ValidationError as e:
        # Attach detailed schema validation error to Allure report
        allure.attach(
            str(e),
            name="Schema Validation Error",
            attachment_type=allure.attachment_type.TEXT,
        )
        # Fail the test with a clear message
        assert False, f"Schema validation failed: {e}"

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
    assert response.status_code == 200 #This will fail intentionally to show the xfail behavior


# -----------------------------------------------
# API Schema Validation Test using Pydantic
# Purpose: Ensure that the API response structure 
# for GET /posts/1 matches the expected schema.
# This helps catch backend contract violations 
# and enforces strong API response validation 
# beyond simple status code checks.
# -----------------------------------------------
class PostModel(BaseModel):
    """ Pydantic model for validating post data structure """
    userId: int
    id: int
    title: str
    body: str

@allure.feature("Posts API")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_post_schema_validation():
    """
    Test: Validate the schema of the retrieved post data
    Purpose: Ensure the API response adheres to the expected schema (positive test)
    Expected Result: HTTP 200 OK, and response matches Pydantic model
    """
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "Expected status code 200 for existing post"

    data = response.json()
    try:
        PostModel(**data)  # Validate against Pydantic model
    except ValidationError as e:
        # Attach detailed schema validation error to Allure report
        allure.attach(
            str(e),
            name="Schema Validation Error",
            attachment_type=allure.attachment_type.TEXT,
        )
        # Fail the test with a clear message
        assert False, f"Schema validation failed: {e}"