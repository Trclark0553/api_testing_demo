# Tests dynamic content loading from https://the-internet.herokuapp.com/dynamic_loading/1
import allure
from playwright.sync_api import sync_playwright

@allure.feature("UI Dynamic Element Tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_dynamic_content_loading():
    """UI Test: Verify content appears after dynamic load completes."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        # Click the "Start" button to load the dynamic content
        page.click("#start button")

        # Wait for the dynamic content ("Hello World!") to appear
        page.wait_for_selector("#finish", timeout=10000)

        assert page.is_visible("#finish"), "Dynamic content did not load as expected."

        text = page.inner_text("#finish")
        assert text == "Hello World!", f"Expected 'Hello World!', but got '{text}'"

        # Attach screenshot to Allure report
        screenshot = page.screenshot()
        allure.attach(screenshot, name="Dynamic Content Screenshot", attachment_type=allure.attachment_type.PNG)

        # Close the browser
        browser.close()