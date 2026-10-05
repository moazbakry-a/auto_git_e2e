
from playwright.sync_api import Page
from base_page import BasePage
from components.login_form import LoginForm


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_form = LoginForm(self.page)
        self.flash_message = self.page.locator("#flash")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")
