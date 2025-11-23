from domain.book import Book
from repositories.book_repository import BookRepository
from typing import Optional

def get_book(repo: BookRepository, book_id: int) -> Optional[Book]:
    return repo.get_by_id(book_id)
