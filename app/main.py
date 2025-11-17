import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

def get_book(book_id):
    connection = get_db_connection()
    book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    connection.close()
    if book is None:
        abort(404)
    return book

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    connection = get_db_connection()
    books = connection.execute('SELECT * FROM books').fetchall()
    connection.close()
    return render_template('index.html', books=books)

@app.route('/<int:book_id>')
def book(book_id):
    book = get_book(book_id)
    return render_template('book.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)