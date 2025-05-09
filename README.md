# API Testing Demo (Pytest + JSONPlaceholder)

This project demonstrates automated API testing using **Python** and **Pytest**, targeting the open [JSONPlaceholder API](https://jsonplaceholder.typicode.com). It covers positive and negative test scenarios for API endpoints, simulating real-world QA automation workflows.

---

## Project Structure
api-testing-demo/
├── .github/workflows/ # (To be added) CI pipeline with GitHub Actions
├── postman/ # (Optional) Postman collection and environment files
├── tests/
│ └── test_api.py # Automated API tests using Pytest
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## Current Test Coverage

- `GET /posts/1`: Validate retrieving a specific post.
- `GET /posts/99999`: Negative test for non-existent post (expects 404).
- `POST /posts`: Validate creating a new post with correct payload.

---

## Notes for Hiring Managers

- Demonstrates **API test automation** using Python and Pytest.
- Follows clean code practices with QA-focused documentation and assertions.
- Shows understanding of **positive and negative testing**.
- Project is structured for easy extension to include CI pipelines and reporting tools.

---

## Install & Run

```bash
pip install -r requirements.txt
pytest tests/
