from typing import List
from domain.book import Book
from repositories.book_repository import BookRepository

def list_books(repo: BookRepository) -> List[Book]:
    return repo.list_all()
