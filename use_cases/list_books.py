from typing import List
from domain.book import Book
from repositories.book_repository import BookRepository

def list_books(repo: BookRepository) -> List[Book]:
    if repo is None:
        raise ValueError("Repositório não pode ser None")
    return repo.list_all()
