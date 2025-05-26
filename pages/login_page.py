# Uses Playwright's Page Object Model (POM) to abstract login page logic, keeps code DRY, and make tests more maintainable.

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = "input#username"
        self.password_field = "input#password"
        self.submit_button = "button#submit"
        self.success_msg = "text= Congratulations student. You successfully logged in!"
        self.error_msg = "text= Invalid username or password."

    def login(self, username, password):
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.submit_button)

    def success_message_displayed(self):
        return self.page.is_visible(self.success_msg)
    
    def error_message_displayed(self):
        return self.page.is_visible(self.error_msg)