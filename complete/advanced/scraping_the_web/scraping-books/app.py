import requests

from pages.all_books_page import AllBooksPage

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books # all_books_page - returns book objects

f = [book for book in books]
print(f)
