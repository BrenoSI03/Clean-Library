from typing import List, Mapping, Any
from repositories.loan_repository import LoanRepository
from infra.db.database import get_db_connection


class LoanRepositorySQLite(LoanRepository):
    def list_books_for_user(self, user_id: int) -> List[Mapping[str, Any]]:
        conn = get_db_connection()
        rows = conn.execute(
            """
            SELECT b.id, b.title, b.author, b.available
            FROM loans l
            JOIN books b ON b.id = l.book_id
            WHERE l.user_id = ?
            """,
            (user_id,),
        ).fetchall()
        conn.close()
        return rows

    def has_active_loan(self, user_id: int, book_id: int) -> bool:
        conn = get_db_connection()
        row = conn.execute(
            "SELECT 1 FROM loans WHERE user_id = ? AND book_id = ?",
            (user_id, book_id),
        ).fetchone()
        conn.close()
        return row is not None

    def borrow_book(self, user_id: int, book_id: int) -> None:
        conn = get_db_connection()
        cur = conn.cursor()

        # Verifica se o livro existe e está disponível
        book_row = cur.execute(
            "SELECT available FROM books WHERE id = ?", (book_id,)
        ).fetchone()

        if book_row is None:
            conn.close()
            raise ValueError("Livro não encontrado")

        if not bool(book_row["available"]):
            conn.close()
            raise ValueError("Livro já está emprestado")

        # Verifica se o usuário já tem esse livro emprestado
        existing = cur.execute(
            "SELECT 1 FROM loans WHERE user_id = ? AND book_id = ?",
            (user_id, book_id),
        ).fetchone()
        if existing is not None:
            conn.close()
            raise ValueError("Esse usuário já possui esse livro emprestado")

        # Cria empréstimo e marca como indisponível
        cur.execute(
            "INSERT INTO loans (book_id, user_id) VALUES (?, ?)",
            (book_id, user_id),
        )
        cur.execute(
            "UPDATE books SET available = 0 WHERE id = ?",
            (book_id,),
        )

        conn.commit()
        conn.close()

    def return_book(self, user_id: int, book_id: int) -> None:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM loans WHERE user_id = ? AND book_id = ?",
            (user_id, book_id),
        )
        cur.execute(
            "UPDATE books SET available = 1 WHERE id = ?",
            (book_id,),
        )

        conn.commit()
        conn.close()

    def list_all(self):
        conn = get_db_connection()
        rows = conn.execute("SELECT * FROM loans").fetchall()
        conn.close()

        return [
            type("Loan", (), {"book_id": row["book_id"], "user_id": row["user_id"]})
            for row in rows
        ]
    
    def has_any_loan(self, book_id: int) -> bool:
        conn = get_db_connection()
        row = conn.execute(
            "SELECT 1 FROM loans WHERE book_id = ? LIMIT 1",
            (book_id,)
        ).fetchone()
        conn.close()
        return row is not None

    def get_loans_by_user(self, user_id: int):
        conn = get_db_connection()
        rows = conn.execute(
            "SELECT * FROM loans WHERE user_id = ?",
            (user_id,)
        ).fetchall()
        conn.close()
        return rows


