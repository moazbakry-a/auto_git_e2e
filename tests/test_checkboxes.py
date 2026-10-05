
from playwright.sync_api import sync_playwright, expect
from checkboxes_page import CheckboxesPage


def test_checkboxes(checkboxes_page):
    checkboxes_page.open()
    expect(checkboxes_page.checkbox1).not_to_be_checked()
    expect(checkboxes_page.checkbox2).to_be_checked()
    checkboxes_page.check_checkbox1()
    checkboxes_page.uncheck_checkbox2()
    expect(checkboxes_page.checkbox1).to_be_checked()
    expect(checkboxes_page.checkbox2).not_to_be_checked()
