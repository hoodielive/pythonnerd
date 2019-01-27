from app import books 

USER_CHOICE = '''
- 'b' to look at 5-star books - 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalog
- 'q' to exit

Enter your choice: '''

user_choices = {
        'b': print_best_books, 
        'c': print_cheapest_books,
        'n': get_next_book
}

def print_best_books():
    best_books = sorted(books, keys=lambda x: x.rating * - 1)[:10] # takes book list from app.py and sorts it (sorted by x.rating)
    f = [book for book in best_books]
    print(f)

def print_cheapest_books():
    cheapest_books = sorted(books, keys=lambda x: x.rating * - 1)[:10] # takes book list from app.py and sorts it (sorted by x.rating)
    f = [book for book in cheapest_books]
    print(f)

books_generator = (x for x in books)

def get_next_book():
    print(next(books_generator))

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)

menu()
