from flask import Blueprint, render_template, request, redirect, url_for, flash
from use_cases.list_books import list_books
from use_cases.get_book import get_book
from use_cases.create_book import create_book
from use_cases.update_book import update_book
from use_cases.delete_book import delete_book
from infra.repositories.book_repository_sqlite import BookRepositorySQLite

# Instanciando o repositório SQLite
book_repo = BookRepositorySQLite()

book_bp = Blueprint("books", __name__, url_prefix="/books")

# ======================== Listar livros ==========================
@book_bp.route("/", methods=["GET"])
def home():
    books = list_books(book_repo)
    return render_template("index.html", books=books)

# ======================== Exibir livro ==========================
@book_bp.route("/<int:book_id>", methods=["GET"])
def book(book_id):
    book = get_book(book_repo, book_id)
    if book is None:
        flash("Livro não encontrado")
        return redirect(url_for("books.home"))
    return render_template("book.html", book=book)

# ======================== Criar livro ==========================
@book_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        available = bool(int(request.form.get("available", "1")))  # Default é 1 (disponível)

        if not title:
            flash("Título é obrigatório!")
        else:
            create_book(book_repo, title, author, available)
            flash("Livro cadastrado com sucesso!")
            return redirect(url_for("books.home"))

    return render_template("create.html")

# ======================== Editar livro ==========================
@book_bp.route("/<int:book_id>/edit", methods=["GET", "POST"])
def edit(book_id):
    book = get_book(book_repo, book_id)
    if book is None:
        flash("Livro não encontrado")
        return redirect(url_for("books.home"))

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        available = bool(int(request.form.get("available", "1")))  # Default é 1 (disponível)

        if not title:
            flash("Título é obrigatório!")
        else:
            update_book(book_repo, book_id, title, author, available)
            flash("Livro atualizado com sucesso!")
            return redirect(url_for("books.home"))

    return render_template("edit.html", book=book)

# ======================== Deletar livro ==========================
@book_bp.route("/<int:book_id>/delete", methods=["POST"])
def delete(book_id):
    delete_book(book_repo, book_id)
    flash("Livro deletado com sucesso!")
    return redirect(url_for("books.home"))
