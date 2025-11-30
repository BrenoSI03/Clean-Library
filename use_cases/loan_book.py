from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository
from repositories.user_repository import UserRepository


def loan_book(
    loan_repo: LoanRepository,
    book_repo: BookRepository,
    user_repo: UserRepository,
    user_id: int,
    book_id: int
) -> None:
    user = user_repo.get_by_id(user_id)
    if user is None:
        raise ValueError("Usuário não encontrado.")

    book = book_repo.get_by_id(book_id)
    if book is None:
        raise ValueError("Livro não encontrado.")

    if not book.available:
        raise ValueError("Este livro está indisponível no momento.")

    if loan_repo.has_active_loan(user_id, book_id):
        raise ValueError("Este usuário já possui este livro emprestado.")

    if loan_repo.has_any_loan(book_id):
        raise ValueError("Livro já está emprestado.")

    loan_repo.borrow_book(user_id, book_id)

    book.available = False
    book_repo.update(book)
