from typing import Optional
from domain.user import User
from repositories.user_repository import UserRepository

def get_user(repo: UserRepository, user_id: int) -> Optional[User]:
    return repo.get_by_id(user_id)
