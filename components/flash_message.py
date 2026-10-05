
class FlashMessage:
    def __init__(self, page):
        self.page = page
        self.message = self.page.locator("#flash")

    def get_text(self):
        return self.message.text_content()
