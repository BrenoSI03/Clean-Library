from typing import Dict, List
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from repositories.loan_repository import LoanRepository


def list_home_dashboard(
    book_repo: BookRepository,
    user_repo: UserRepository,
    loan_repo: LoanRepository,
) -> Dict[str, List]:
    # 1) Carrega livros e usuários
    books = book_repo.list_all()
    users = user_repo.list_all()

    # 2) Carrega todos os empréstimos
    all_loans = loan_repo.list_all()  # retorna objetos com book_id e user_id

    loaned_book_ids = {loan.book_id for loan in all_loans}

    # 3) Marca quais livros estão emprestados
    for book in books:
        book.is_loaned = book.id in loaned_book_ids

    # 4) Monta lista de empréstimos com dados de livro e usuário
    loans = []
    for loan in all_loans:
        book = book_repo.get_by_id(loan.book_id)
        user = user_repo.get_by_id(loan.user_id)
        if book is None or user is None:
            continue

        loans.append({
            "book_id": book.id,
            "title": book.title,
            "author": book.author,
            "user_id": user.id,
            "user_name": user.name,
        })

    return {
        "books": books,
        "users": users,
        "loans": loans,
    }
