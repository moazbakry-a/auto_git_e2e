from playwright.sync_api import sync_playwright, expect
from login_page import LoginPage


def test_login_valid(login_page):
    login_page.open()
    login_page.login_form.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.flash_message).to_contain_text(
        "You logged into a secure area!")
    login_page.login_form.logout()
    login_page.login_form.login("wrongusername", "SuperSecretPassword!")
    expect(login_page.flash_message).to_contain_text(
        "Your username is invalid!")
    login_page.login_form.login("tomsmith", "wrongpassword")
    expect(login_page.flash_message).to_contain_text(
        "Your password is invalid!")
