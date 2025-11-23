from flask import Blueprint, render_template, request, redirect, url_for, flash
from use_cases.list_users import list_users
from use_cases.get_user import get_user
from use_cases.create_user import create_user
from use_cases.update_user import update_user
from use_cases.delete_user import delete_user
from infra.repositories.user_repository_sqlite import UserRepositorySQLite

# Instanciando o repositório SQLite de usuários
user_repo = UserRepositorySQLite()

user_bp = Blueprint("users", __name__, url_prefix="/users")

# ======================== Listar usuários ==========================
@user_bp.route("/", methods=["GET"])
def home():
    users = list_users(user_repo)
    return render_template("users/index.html", users=users)

# ======================== Exibir usuário ==========================
@user_bp.route("/<int:user_id>", methods=["GET"])
def user(user_id):
    user = get_user(user_repo, user_id)
    if user is None:
        flash("Usuário não encontrado")
        return redirect(url_for("users.home"))
    return render_template("users/user.html", user=user)

# ======================== Criar usuário ==========================
@user_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]

        if not name:
            flash("Nome é obrigatório!")
        else:
            create_user(user_repo, name)
            flash("Usuário cadastrado com sucesso!")
            return redirect(url_for("users.home"))

    return render_template("users/create.html")

# ======================== Editar usuário ==========================
@user_bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
def edit(user_id):
    user = get_user(user_repo, user_id)
    if user is None:
        flash("Usuário não encontrado")
        return redirect(url_for("users.home"))

    if request.method == "POST":
        name = request.form["name"]

        if not name:
            flash("Nome é obrigatório!")
        else:
            update_user(user_repo, user_id, name)
            flash("Usuário atualizado com sucesso!")
            return redirect(url_for("users.home"))

    return render_template("users/edit.html", user=user)

# ======================== Deletar usuário ==========================
@user_bp.route("/<int:user_id>/delete", methods=["POST"])
def delete(user_id):
    delete_user(user_repo, user_id)
    flash("Usuário deletado com sucesso!")
    return redirect(url_for("users.home"))
