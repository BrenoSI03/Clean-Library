from domain.entities.book import Book
from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository

def loan_book(loan_repo: LoanRepository, book_repo: BookRepository, user_id: int, book_id: int):
    book = book_repo.get_by_id(book_id)

    if book is None:
        raise ValueError("Livro não encontrado.")

    if not book.available:
        raise ValueError("Este livro está indisponível no momento.")

    # Verificar se o usuário já pegou esse livro
    if loan_repo.has_active_loan(user_id, book_id):
        raise ValueError("Este livro já está emprestado.")

    # Criar empréstimo
    loan_repo.loan_book(user_id, book_id)

    # Atualizar disponibilidade
    book.available = False
    book_repo.update(book)
