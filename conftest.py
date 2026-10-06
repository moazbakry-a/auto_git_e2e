import pytest
from playwright.sync_api import sync_playwright
from login_page import LoginPage
from checkboxes_page import CheckboxesPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture              # login_page = LoginPage(page)
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def checkboxes_page(page):
    return CheckboxesPage(page)
