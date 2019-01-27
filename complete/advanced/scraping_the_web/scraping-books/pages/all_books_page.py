from bs4 import BeautifulSoup
from locators.book_page_locator import AllBooksPageLocators
#from parsers.book import BookParser

class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)
