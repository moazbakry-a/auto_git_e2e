
from playwright.sync_api import sync_playwright, expect


def test_checkboxes(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox1 = page.locator("input[type='checkbox']").nth(0)
    checkbox2 = page.locator("input[type='checkbox']").nth(1)
    expect(checkbox1).not_to_be_checked()
    expect(checkbox2).to_be_checked()
    checkbox1.check()
    checkbox2.uncheck()
    expect(checkbox1).to_be_checked()
    expect(checkbox2).not_to_be_checked()
