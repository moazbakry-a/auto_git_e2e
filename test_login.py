from playwright.sync_api import sync_playwright, expect
from login_page import LoginPage


def test_login_valid(login_page):
    login_page.open()
    login_page.login_form.login("tomsmith", "SuperSecretPassword!")
    message = login_page.flash_message.get_text()
    assert "You logged into a secure area!" in message
    login_page.login_form.logout()
    login_page.login_form.login("wrongusername", "SuperSecretPassword!")
    message = login_page.flash_message.get_text()
    assert "Your username is invalid!" in message
    login_page.login_form.login("tomsmith", "wrongpassword")
    message = login_page.flash_message.get_text()
    assert "Your password is invalid!" in message
