import sqlite3

"""
Concerned with storing and retrieving books from a sqlite3 database
"""

def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    # SQLite supports 5 datatypes: null, integers, real(floating point), text(str), blobs(binary data field)
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    connection.commit()
    connection.close()

def add_book(name, author):
    # ",0); DROP TABLE books; <--- SQL INJECTION ATTACK ---> So don't don't do the f'string shit
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[3]} for row in cursor.fetchall()]
    connection.close() 
    return books

def _save_all_books(books):
    pass

def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
    connection.commit()
    connection.close()

def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?', (name,))
    connection.commit()
    connection.close()
