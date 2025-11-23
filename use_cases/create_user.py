from domain.user import User
from repositories.user_repository import UserRepository

def create_user(repo: UserRepository, name: str) -> User:
    return repo.create(name)
