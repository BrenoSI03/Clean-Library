from abc import ABC, abstractmethod
from typing import List, Optional
from domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def list_all(self) -> List[User]:
        """
        Retorna uma lista de todos os usuários.
        """
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        """
        Retorna um usuário pelo ID. Se não encontrado, retorna None.
        """
        pass

    @abstractmethod
    def create(self, name: str) -> User:
        """
        Cria um novo usuário e retorna a instância do usuário.
        """
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        """
        Atualiza um usuário existente.
        """
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        """
        Deleta um usuário pelo ID.
        """
        pass
