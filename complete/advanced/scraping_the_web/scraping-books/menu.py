from app import books 

def print_best_books():
    best_books = sorted(books, keys=lambda x: x.rating * - 1)[:10] # takes book list from app.py and sorts it (sorted by x.rating)
    f = [book for book in best_books]
    print(f)

print_best_books()
