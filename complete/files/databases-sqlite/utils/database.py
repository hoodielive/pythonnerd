"""
Concerned with storing and retrieving books from a list/array
"""

books = []

def add_book(name, author):
    books.append({ 'name': name, 'author': author, 'read': False })

# def prompt_add_book() # ask for book name and author 
# def list_books() # show all the books in our list
# def prompt_read_book() # ask for a book name and change it to read in our list
# def prompt_delete_book() # ask for book name and remove book from list
