from repositories.user_repository import UserRepository

def delete_user(repo: UserRepository, user_id: int) -> None:
    user = repo.get_by_id(user_id)
    if user is None:
        raise ValueError("Usuário não encontrado")

    repo.delete(user_id)
