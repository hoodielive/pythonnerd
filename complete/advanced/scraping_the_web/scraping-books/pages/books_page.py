from bs4 import BeautifulSoup
from locators.book_page_locator import BookPageLocator
from parsers.book import BookParser

class BookPage:
    def __init__(self, page):
        soup = BeautifulSoup(page, 'html.parser')

    def book(self):
        locator = BookPageLocator.BOOK
        
