from typing import List
from domain.user import User
from repositories.user_repository import UserRepository

def list_users(repo: UserRepository) -> List[User]:
    return repo.list_all()
