

from base_page import BasePage


class CheckBoxesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkbox1 = self.page.locator("input[type='checkbox']").nth(0)
        self.checkbox2 = self.page.locator("input[type='checkbox']").nth(1)

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def check_checkbox1(self):
        self.checkbox1.check()

    def uncheck_checkbox2(self):
        self.checkbox2.uncheck()
