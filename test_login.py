from playwright.sync_api import sync_playwright, expect
from login_page import LoginPage
from test_data.login_data import login_cases
import pytest


@pytest.mark.parametrize("username,password,expected_message", login_cases)
def test_login(login_page, username, password, expected_message):
    login_page.open()
    login_page.login_form.login(username, password)
    message = login_page.flash_message.get_text()
    assert expected_message in message
