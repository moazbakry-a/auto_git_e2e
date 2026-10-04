from playwright.sync_api import sync_playwright, expect


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com")
        page.get_by_role("link", name="Form Authentication").click()
        page.get_by_label("Username").fill("tomsmith")
        page.get_by_label("Password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="Login").click()
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
        flash_message = page.locator("#flash")
        expect(flash_message).to_contain_text("You logged into a secure area!")
        browser.close()
