from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository

def delete_book(book_repo: BookRepository, loan_repo: LoanRepository, book_id: int) -> None:
    if loan_repo.has_any_loan(book_id):
        raise ValueError("Não é permitido deletar um livro que está emprestado.")

    book = book_repo.get_by_id(book_id)
    if book is None:
        raise ValueError("Livro não encontrado")

    book_repo.delete(book_id)
