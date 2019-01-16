"""
Concerned with storing and retrieving books from a list/array
"""

books = []

def add_book(name, author):
    books.append({ 'name': name, 'author': author, 'read': False })

def get_all_books():
    return books


