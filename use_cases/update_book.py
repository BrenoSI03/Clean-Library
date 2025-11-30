from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository
from domain.book import Book

def update_book(book_repo: BookRepository, loan_repo: LoanRepository, book_id: int, title: str, author: str, available: bool) -> Book:
    book = book_repo.get_by_id(book_id)
    if book is None:
        raise ValueError("Book not found")
    
    if loan_repo.has_any_loan(book_id):
        if available != book.available:
            raise ValueError("Não é permitido alterar a disponibilidade de um livro emprestado.")

    book.title = title
    book.author = author

    if not loan_repo.has_any_loan(book_id):
        book.available = available

    book_repo.update(book)
    return book
