from flask import Blueprint, render_template, request, redirect, url_for, flash
from use_cases.list_users import list_users
from use_cases.get_user import get_user
from use_cases.create_user import create_user
from use_cases.update_user import update_user
from use_cases.delete_user import delete_user
from use_cases.list_user_loans import list_books_for_user

from infra.repositories.user_repository_sqlite import UserRepositorySQLite
from infra.repositories.loan_repository_sqlite import LoanRepositorySQLite

user_repo = UserRepositorySQLite()
loan_repo = LoanRepositorySQLite()

user_bp = Blueprint("users", __name__, url_prefix="/users")


# ====== Listar usuários ======
@user_bp.route("/", methods=["GET"])
def home():
    users = list_users(user_repo)
    loans = []
    
    # Listando empréstimos de livros
    for user in users:
        borrowed_books = list_books_for_user(loan_repo, user.id)
        for book in borrowed_books:
            loans.append({
                'book_id': book['id'],
                'title': book['title'],
                'author': book['author'],
                'user_name': user.name,
                'user_id': user.id,
            })

    return render_template("index.html", users=users, loans=loans)



# ====== Detalhe do usuário + livros emprestados ======
@user_bp.route("/<int:user_id>", methods=["GET"])
def user(user_id):
    u = get_user(user_repo, user_id)
    if u is None:
        flash("Usuário não encontrado")
        return redirect(url_for("home"))

    borrowed_books = list_books_for_user(loan_repo, user_id)
    return render_template("users/user.html", user=u, borrowed_books=borrowed_books)


# ====== Criar usuário ======
@user_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]

        if not name:
            flash("Nome é obrigatório!")
        else:
            create_user(user_repo, name)
            flash("Usuário cadastrado com sucesso!")
            return redirect(url_for("home"))

    return render_template("users/create.html")


# ====== Editar usuário ======
@user_bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
def edit(user_id):
    user = get_user(user_repo, user_id)

    if user is None:
        flash("Usuário não encontrado")
        return redirect(url_for("home"))
    
    user_loans = loan_repo.get_loans_by_user(user_id)

    if user_loans is None:
        user_loans = []

    user.has_loans = len(user_loans) > 0

    if request.method == "POST":
        name = request.form["name"]

        if not name:
            flash("Nome é obrigatório!")
        else:

            try:
                update_user(user_repo, user_id, name)
                flash("Usuário atualizado com sucesso!")
            except ValueError as e:
                flash(str(e), "error")

            return redirect(url_for("users.edit", user_id=user_id))

    return render_template("users/edit.html", user=user)


# ====== Deletar usuário ======
@user_bp.route("/<int:user_id>/delete", methods=["POST"])
def delete(user_id):
    try:
        delete_user(user_repo, loan_repo, user_id)
        flash("Usuário deletado com sucesso!")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("home"))
