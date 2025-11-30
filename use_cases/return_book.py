from repositories.loan_repository import LoanRepository
from repositories.book_repository import BookRepository


def return_book(loan_repo: LoanRepository, book_repo: BookRepository, user_id: int, book_id: int) -> None:
    if not loan_repo.has_active_loan(user_id, book_id):
        raise ValueError("Este livro não está emprestado para este usuário.")

    loan_repo.return_book(user_id, book_id)

    book = book_repo.get_by_id(book_id)
    if book is None:
        raise ValueError("Livro não encontrado.")
    book.available = 1
    book_repo.update(book)
