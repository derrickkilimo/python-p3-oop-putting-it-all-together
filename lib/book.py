#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=None):
        self.title = title
        self._page_count = 0
        if page_count is not None:
            self.page_count = page_count

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page_count, set_page_count)

book = Book("And Then There Were None")
book.page_count = 90  # Use the property setter
print(book.page_count)  # Use the property getter
book.turn_page()
