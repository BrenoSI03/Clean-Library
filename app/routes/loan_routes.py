from flask import Blueprint, redirect, url_for, flash
from use_cases.return_book import return_book  # O caso de uso para devolver o livro
from infra.repositories.loan_repository_sqlite import LoanRepositorySQLite
from infra.repositories.book_repository_sqlite import BookRepositorySQLite

# Instanciando os repositórios
loan_repo = LoanRepositorySQLite()
book_repo = BookRepositorySQLite()

loan_bp = Blueprint('loans', __name__, url_prefix='/loans')

@loan_bp.route("/<int:user_id>/returns/<int:book_id>", methods=["POST"])
def return_book_route(user_id, book_id):
    try:
        return_book(loan_repo, book_repo, user_id, book_id)
        flash("Livro devolvido com sucesso!")
    except ValueError as e:
        flash(str(e))
    return redirect(url_for("home", user_id=user_id))

