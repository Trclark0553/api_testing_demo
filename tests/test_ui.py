import allure
from playwright.sync_api import sync_playwright

@allure.feature("UI Smoke Test")
@allure.severity(allure.severity_level.CRITICAL)
def test_homepage_title():
    """ UI Test: Verify the page title of example.com """
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")

        # Attach a screenshot to Allure report
        screenshot = page.screenshot()
        allure.attach(screenshot, name="homepage screenshot", attachment_type=allure.attachment_type.PNG)

        assert page.title() == "Example Domain", "Page title does not match expected value"

        # Close the browser
        browser.close()
        
@allure.feature("UI Smoke Test")
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_click():
    """ UI Test: Click a link and verify navigation """
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")

        # Click the "More information..." link
        page.click("text=More information...")

        # Attach a screenshot to Allure report
        screenshot = page.screenshot()
        allure.attach(screenshot, name="navigation screenshot", attachment_type=allure.attachment_type.PNG)

        # Verify navigation to the expected page(example.org is used for demo)
        assert "iana.org" in page.url, "Navigation did not lead to expected URL"

        # Close the browser
        browser.close()
