from flask import Flask, render_template, redirect, url_for
from app.routes.book_routes import book_bp
from app.routes.user_routes import user_bp
from infra.repositories.book_repository_sqlite import BookRepositorySQLite
from infra.repositories.user_repository_sqlite import UserRepositorySQLite
from infra.repositories.loan_repository_sqlite import LoanRepositorySQLite
from use_cases.list_books import list_books
from use_cases.list_users import list_users
from use_cases.list_user_loans import list_books_for_user

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = "grXBaIz0Ag0a7XllLUI3maScR7mbnFZC"

# Instanciando os repositórios
book_repo = BookRepositorySQLite()
user_repo = UserRepositorySQLite()
loan_repo = LoanRepositorySQLite()

@app.route('/', methods=["GET"])
def home():
    books = list_books(book_repo)
    users = list_users(user_repo)
    
    loans = []
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

    return render_template('index.html', books=books, users=users, loans=loans)

app.register_blueprint(book_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)
