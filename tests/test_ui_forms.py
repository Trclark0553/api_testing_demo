#This demonstates dynamic testing of Forms using Playwright (also attaches info to Allure report)
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  # Assuming you have a page object model for the login page

@allure.feature("UI Form Tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_form_success():
    """ UI Test: Validate successful login using Page Object Model (POM) with Playwright """
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # Use the LoginPage object to interact with the login form
        login_page = LoginPage(page)
        login_page.login("student", "Password123")
        
        # Validate successful login by checking the success message
        assert login_page.success_message_displayed(), "Login was not successful, success message not found."

        # Take a screenshot of the result for Allure report
        screenshot = page.screenshot()
        allure.attach(screenshot, name="Login Success Screenshot", attachment_type=allure.attachment_type.PNG)

        # Close the browser
        browser.close()

@allure.feature("UI Form Tests")
@allure.severity(allure.severity_level.NORMAL)
def test_login_form_failure():
    """ UI Test: Validate failed login using Page Object Model """
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # Use the LoginPage object to interact with the login form
        login_page = LoginPage(page)
        login_page.login("wronguser", "wrongpass")

        # Validate failed login by checking the error message
        assert login_page.error_message_displayed(), "Login was successful, but it should have failed."

        # Take a screenshot of the result for Allure report
        screenshot = page.screenshot()
        allure.attach(screenshot, name="Login Failure Screenshot", attachment_type=allure.attachment_type.PNG)

        # Close the browser
        browser.close()

        