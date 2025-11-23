from abc import ABC, abstractmethod
from typing import List, Optional
from domain.book import Book

class BookRepository(ABC):

    @abstractmethod
    def list_all(self) -> List[Book]:
        """
        Retorna uma lista de todos os livros.
        """
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        """
        Retorna um livro pelo ID. Se não encontrado, retorna None.
        """
        pass

    @abstractmethod
    def create(self, title: str, author: str, available: bool) -> Book:
        """
        Cria um novo livro e retorna a instância do livro.
        """
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        """
        Atualiza um livro existente.
        """
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        """
        Deleta um livro pelo ID.
        """
        pass
