from typing import List, Mapping, Any
from repositories.loan_repository import LoanRepository


def list_books_for_user(loan_repo: LoanRepository, user_id: int) -> List[Mapping[str, Any]]:
    return loan_repo.list_books_for_user(user_id)
