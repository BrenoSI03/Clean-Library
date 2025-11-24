from repositories.user_repository import UserRepository
from repositories.loan_repository import LoanRepository


def return_book(user_repo: UserRepository, loan_repo: LoanRepository, user_id: int, book_id: int) -> None:
    user = user_repo.get_by_id(user_id)
    if user is None:
        raise ValueError("Usuário não encontrado")

    loan_repo.return_book(user_id, book_id)
