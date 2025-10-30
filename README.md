![CI Status](https://github.com/Trclark0553/api_testing_demo/actions/workflows/ci.yaml/badge.svg)

---

# API & UI Testing Demo (Pytest + Playwright + Allure Reporting + GitHub Actions CI)

This project demonstrates professional test automation for APIs using **Python**, **Pytest**, and **Allure Reporting**, with a fully automated **CI/CD pipeline using GitHub Actions**. It also integrates **Pydantic** for API schema validation and publishes clean, visual test reports via **GitHub Pages**.

---

## Goal

- To demonstrates full-stack QA automation with both API and UI test coverage.
- Show real-world CI/CD pipeline configuration and Allure reporting integration.
- Highlight structured, maintainable test code using best practices and modern tools.

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
├── pages/                         # Page Object Model components for UI tests
│   ├── __init__.py
│   └── login_page.py              # Reusable login page class
├── tests/
│   ├── test_api.py                # API functional and schema validation tests
│   ├── test_ui.py                 # UI smoke tests (homepage and navigation)
│   ├── test_ui_forms.py           # UI form tests using POM
│   └── test_ui_dynamic.py         # UI test for dynamic loading elements
├── requirements.txt # project dependencies
└── README.md # Project documentation
```

---

## Current Test Coverage

- **API Functional Tests:**
  - Parameterized positive and negative scanarios for REST API endpoints.
  - Data-driven request validation with diverse input combinations.
  - Clean separation of happy path and error path testing.
- **API Schema Validation:**
  - Validates API response structure using both **Pydantic** and **JSONSchema** models.
  - Demonstates tool flexibility for schem enforcement across Python-based as well as external APIs.
  - Schema failures are logged with detailed messages in the Allure report.
- **UI Automation Tests (Playwright):**
  - Homepage title verification and navigation tests.
  - Positive and negative form submission scenarios using Page Object Model (POM).
  - Resuable page class design improves test maintainability and readability.
  - Includes dynamic UI tests with wait conditions and async element handling.
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

- Add UI automation coverage for modals, dropdowns, and file uploads.
- Integrate test data management with fixtures or factories.
- Explore Allure's trend reporting with historical test results. (Do this next).
- Package project as a template or starter kit for other QA engineers if desired.

---
