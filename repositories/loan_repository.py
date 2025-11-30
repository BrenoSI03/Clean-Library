from abc import ABC, abstractmethod
from typing import List, Mapping, Any


class LoanRepository(ABC):
    @abstractmethod
    def list_books_for_user(self, user_id: int) -> List[Mapping[str, Any]]:
        """Retorna os livros atualmente emprestados para um usuário."""
        pass

    @abstractmethod
    def has_active_loan(self, user_id: int, book_id: int) -> bool:
        """Verifica se esse usuário já tem esse livro emprestado."""
        pass

    @abstractmethod
    def borrow_book(self, user_id: int, book_id: int) -> None:
        """Cria o empréstimo e marca o livro como indisponível."""
        pass

    @abstractmethod
    def return_book(self, user_id: int, book_id: int) -> None:
        """Remove o empréstimo e marca o livro como disponível."""
        pass

    @abstractmethod
    def has_any_loan(self, book_id: int) -> bool:
        """Verifica se o livro está emprestado para algum usuário."""
        pass

    @abstractmethod
    def get_loans_by_user(self, user_id: int):
        """Retorna todos os empréstimos de um usuário."""
        pass
