from abc import ABC, abstractmethod
from domain.entities.book import Book

class BookRepository(ABC):

    @abstractmethod
    def add(self, book: Book) -> Book:
        pass

    @abstractmethod
    def list_all(self) -> list[Book]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Book | None:
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        pass
