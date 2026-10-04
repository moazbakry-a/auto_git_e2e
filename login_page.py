
from playwright.sync_api import Page
from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.flash_message = page.locator("#flash")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_link.click()
