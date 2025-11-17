import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
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
app.config['SECRET_KEY'] = 'grXBaIz0Ag0a7XllLUI3maScR7mbnFZC'

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

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        available = request.form['available']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO books (title, author, available) VALUES (?, ?, ?)',
                               (title, author, available))
            connection.commit()
            connection.close()
            return redirect(url_for('home'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)