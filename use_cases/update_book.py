from repositories.book_repository import BookRepository
from domain.book import Book

def update_book(repo: BookRepository, book_id: int, title: str, author: str, available: bool) -> Book:
    book = repo.get_by_id(book_id)
    if book is None:
        raise ValueError("Book not found")

    book.title = title
    book.author = author
    book.available = available
    repo.update(book)
    return book
