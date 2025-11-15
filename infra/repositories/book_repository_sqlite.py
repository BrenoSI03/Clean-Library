import sqlite3
from domain.entities.book import Book
from domain.repositories.book_repository import BookRepository

class BookRepositorySQLite(BookRepository):

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def add(self, book: Book) -> Book:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)",
                       (book.title, book.author, book.available))
        self.conn.commit()
        book.id = cursor.lastrowid
        return book

    def list_all(self) -> list[Book]:
        cursor = self.conn.cursor()
        rows = cursor.execute("SELECT id, title, author, available FROM books").fetchall()
        return [Book(*row) for row in rows]

    def get_by_id(self, book_id: int) -> Book | None:
        cursor = self.conn.cursor()
        row = cursor.execute(
            "SELECT id, title, author, available FROM books WHERE id=?",
            (book_id,)
        ).fetchone()
        return Book(*row) if row else None

    def update(self, book: Book):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE books SET title=?, author=?, available=? WHERE id=?",
            (book.title, book.author, book.available, book.id)
        )
        self.conn.commit()
