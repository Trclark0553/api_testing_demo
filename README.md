![CI Status](https://github.com/Trclark0553/api_testing_demo/actions/workflows/ci.yaml/badge.svg)

---

# API & UI Testing Demo (Pytest + Playwright + Allure Reporting + GitHub Actions CI)

This project demonstrates professional test automation for APIs using **Python**, **Pytest**, and **Allure Reporting**, with a fully automated **CI/CD pipeline using GitHub Actions**. It also integrates **Pydantic** for API schema validation and publishes clean, visual test reports via **GitHub Pages**.

---

## Notes for Hiring Managers

- Demonstrates full-stack QA automation with both API and UI test coverage.
- Shows real-world CI/CD pipeline configuration and Allure reporting integration.
- Highlights structured, maintainable test code using best practices and modern tools.

---

## Live Test Report

[**View the Latest Allure Report Here**](https://trclark0553.github.io/api_testing_demo/)

> _This report is automatically updated after every successful pipeline run._

---

## 📂 Project Structure

```
api-testing-demo/
├── .github/workflows/ci.yml # CI pipeline definition
├── postman/ # (In Progress) Postman API collections
├── tests/
│ ├── test_api.py # API functional tests
│ ├── test_ui.py # UI smoke tests (homepage and navigation)
│ └── test_ui_forms.py # UI form interaction tests (login scenarios)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## Current Test Coverage

- **API Functional Tests:**
  - Parameterized positive and negative scanarios for REST API endpoints.
  - Data-driven request validation with diverse input combinations.
  - Clean separation of happy path and error path testing.
- **API Schema Validation:**
  - Validates API response structure using **Pydantic** models.
  - Fails gracefully with detailed Allure report attachments.
- **UI Automation Tests (Playwright):**
  - Homepage title verification and navigation tests.
  - Positive and negative form submission scenarios with screenshot attachments.
  - Fully integrated with Allure reporting and CI pipeline.
- **Allure Reporting:**
  - Integrated with CI pipeline and available via GitHub Pages.
  - Includes metadata tagging, severity levels, and failure attachments.
- **CI/CD Pipeline:**
  - Fully automated using **GitHub Actions**.
  - Publishes HTML reports as downloadable artifacts and live web reports.
  
---

## For running tests locally

```bash
pip install -r requirements.txt
playwright install
pytest --alluredir=allure-results
allure serve allure-results  # Requires Allure CLI installed
```

---

## Planned Enhancements

- Add API schema validation using `jsonschema` for broader tool exposure.
- Explore test data management and historical reporting for Allure.
- Add additional UI scenarios with dynamic elements and conditional waits.

---
