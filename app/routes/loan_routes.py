from flask import Blueprint, redirect, url_for, flash, request
from use_cases.loan_book import loan_book
from use_cases.return_book import return_book
from infra.repositories.loan_repository_sqlite import LoanRepositorySQLite
from infra.repositories.book_repository_sqlite import BookRepositorySQLite
from infra.repositories.user_repository_sqlite import UserRepositorySQLite

loan_repo = LoanRepositorySQLite()
book_repo = BookRepositorySQLite()
user_repo = UserRepositorySQLite()

loan_bp = Blueprint("loans", __name__, url_prefix="/loans")


@loan_bp.route("/<int:user_id>/borrow", methods=["POST"])
def borrow_book_route(user_id: int):
    try:
        # book_id vem do formulário
        book_id = int(request.form["book_id"])

        loan_book(loan_repo, book_repo, user_repo, user_id, book_id)
        flash("Livro emprestado com sucesso!", "success")
    except ValueError as e:
        flash(str(e), "error")

    return redirect(url_for("users.user", user_id=user_id))


@loan_bp.route("/<int:user_id>/returns/<int:book_id>", methods=["POST"])
def return_book_route(user_id: int, book_id: int):
    try:
        return_book(loan_repo, book_repo, user_id, book_id)
        flash("Livro devolvido com sucesso!", "success")
    except ValueError as e:
        flash(str(e), "error")

    return redirect(url_for("home"))
