#This demonstates dynamic testing of Forms using Playwright (also attaches info to Allure report)
import allure
from playwright.sync_api import sync_playwright

@allure.feature("UI Form Tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_form_success():
    """ UI Test: Validate successful login on practice test site """
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # Fill out login form
        page.fill("input#username", "student")
        page.fill("input#password", "Password123")
        page.click("button#submit")

        # Validate successful login by checking the URL or a success message
        assert "practicetestautomation.com/logged-in-successfully/" in page.url, "Did not navigate to the expected URL after login"
        assert page.is_visible("text=Congratulations student. You successfully logged in!"), "Success message not found."

        # Take a screenshot of the result for Allure report
        screenshot = page.screenshot()
        allure.attach(screenshot, name="Login Success Screenshot", attachment_type=allure.attachment_type.PNG)

        # Close the browser
        browser.close()

@allure.feature("UI Form Tests")
@allure.severity(allure.severity_level.NORMAL)
def test_login_form_failure():
    """ UI Test: Validate failed login with incrorrect credentials """
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # Fill out login form with incorrect credentials
        page.fill("input#username", "wronguser")
        page.fill("input#password", "wrongpass")
        page.click("button#submit")

        # Validate failed login by checking the error message
        assert page.is_visible("text=Your username is invalid!") or page.is_visible("text=Your password is invalid!"), "Expected error message not found."

        # Take a screenshot of the result for Allure report
        screenshot = page.screenshot()
        allure.attach(screenshot, name="Login Failure Screenshot", attachment_type=allure.attachment_type.PNG)

        # Close the browser
        browser.close()

        