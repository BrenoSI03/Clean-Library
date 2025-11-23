from typing import List, Optional
from domain.book import Book
from repositories.book_repository import BookRepository
from infra.db.database import get_db_connection

class BookRepositorySQLite(BookRepository):

    def list_all(self) -> List[Book]:
        conn = get_db_connection()
        rows = conn.execute("SELECT * FROM books").fetchall()
        conn.close()
        return [Book(id=row["id"], title=row["title"], author=row["author"], available=bool(row["available"])) for row in rows]

    def get_by_id(self, book_id: int) -> Optional[Book]:
        conn = get_db_connection()
        row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
        conn.close()
        if row is None:
            return None
        return Book(id=row["id"], title=row["title"], author=row["author"], available=bool(row["available"]))

    def create(self, title: str, author: str, available: bool) -> Book:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", (title, author, int(available)))
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        return Book(id=new_id, title=title, author=author, available=available)

    def update(self, book: Book) -> None:
        conn = get_db_connection()
        conn.execute("UPDATE books SET title = ?, author = ?, available = ? WHERE id = ?", (book.title, book.author, int(book.available), book.id))
        conn.commit()
        conn.close()

    def delete(self, book_id: int) -> None:
        conn = get_db_connection()
        conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
