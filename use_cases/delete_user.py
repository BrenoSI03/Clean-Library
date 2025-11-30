from repositories.user_repository import UserRepository
from repositories.loan_repository import LoanRepository

def delete_user(user_repo: UserRepository, loan_repo: LoanRepository, user_id: int) -> None:
    user = user_repo.get_by_id(user_id)
    if user is None:
        raise ValueError("Usuário não encontrado")
    
    loans = loan_repo.get_loans_by_user(user_id)
    if len(loans) > 0:
        raise ValueError("Não é permitido deletar um usuário com empréstimos ativos.")

    user_repo.delete(user_id)
