from domain.book import Book
from repositories.book_repository import BookRepository

def create_book(repo: BookRepository, title: str, author: str, available: bool) -> Book:
    return repo.create(title, author, available)
