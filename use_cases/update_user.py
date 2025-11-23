from domain.user import User
from repositories.user_repository import UserRepository

def update_user(repo: UserRepository, user_id: int, name: str) -> User:
    user = repo.get_by_id(user_id)
    if user is None:
        raise ValueError("User not found")
    user.name = name
    repo.update(user)
    return user
