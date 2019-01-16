from utils import database

USER_CHOICE = """
- 'a' to add a new book
- 'l' to list all books 
- 'r' to mark a book as read
- 'd' to delete a book 
- 'q' to quit

Your choice:"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown option selected. Please try again.")
        user_input = input(USER_CHOICE)

# def prompt_add_book() # ask for book name and author 
def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the name of the author: ')
    database.add_book(name, author)

# def list_books() # show all the books in our list
def list_books():
    books = database.get_all_books()
    for book in books:
        print(f"{book['name']} by {book['author']}, read: {book['read']}")

# def prompt_read_book() # ask for a book name and change it to read in our list
def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    database.mark_book_as_read(name)

# def prompt_delete_book() # ask for book name and remove book from list
def delete_book(name):
    database.delete_book(name)

