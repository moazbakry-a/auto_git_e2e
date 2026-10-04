
class BasePage:
    def __init__(self, page):
        self.page = page

    def go_back(self):
        self.page.go_back()

    def refresh(self):
        self.page.reload()

    def current_url(self):
        return self.page.url
