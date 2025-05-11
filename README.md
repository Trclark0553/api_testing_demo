![CI Status](https://github.com/Trclark0553/api_testing_demo/actions/workflows/ci.yml/badge.svg)

---

# API & UI Testing Demo (Pytest + Playwright + Allure Reporting + GitHub Actions CI)

This project demonstrates professional test automation for APIs using **Python**, **Pytest**, and **Allure Reporting**, with a fully automated **CI/CD pipeline using GitHub Actions**. It also integrates **Pydantic** for API schema validation and publishes clean, visual test reports via **GitHub Pages**.

---

## Notes for Hiring Managers

- Demonstrates advanced QA automation capabilities with API and reporting integrations.
- Shows real-world CI/CD pipeline configuration with automated test execution and reporting.
- Highlights structured, maintainable test code using best practices and modern tools.

---

## Live Test Report

[**View the Latest Allure Report Here**](https://trclark0553.github.io/api_testing_demo/)

> _This report is automatically updated after every successful pipeline run._

---

## 📂 Project Structure

```
api-testing-demo/
├── .github/workflows/ci.yml      # CI pipeline definition
├── postman/                      # (Not yet implemented) Postman API collections
├── tests/                        # Automated tests (API, Schema Validation)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## Current Test Coverage

- **API Functional Tests:**
  - Positive and negative scenarios for REST API endpoints.
  - Request validation and response content checks.
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

- Introduce **UI Automation Testing** with Selenium or Playwright.
- Integrate UI tests into the same CI pipeline with unified Allure reporting.
- Add API schema validation using `jsonschema` for broader tool exposure.
- Explore test data management and parameterization for more scalable testing.

---
