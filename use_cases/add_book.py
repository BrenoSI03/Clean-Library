from domain.entities.book import Book
from domain.repositories.book_repository import BookRepository

class AddBookUseCase:

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, title: str, author: str) -> Book:
        book = Book(id=None, title=title, author=author)
        return self.repository.add(book)
