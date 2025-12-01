from flask import Flask, render_template
from app.routes.book_routes import book_bp
from app.routes.user_routes import user_bp
from app.routes.loan_routes import loan_bp
from infra.repositories.book_repository_sqlite import BookRepositorySQLite
from infra.repositories.user_repository_sqlite import UserRepositorySQLite
from infra.repositories.loan_repository_sqlite import LoanRepositorySQLite
from use_cases.list_home_dashboard import list_home_dashboard

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = "grXBaIz0Ag0a7XllLUI3maScR7mbnFZC"

book_repo = BookRepositorySQLite()
user_repo = UserRepositorySQLite()
loan_repo = LoanRepositorySQLite()


@app.route("/", methods=["GET"])
def home():
    data = list_home_dashboard(book_repo, user_repo, loan_repo)
    return render_template(
        "index.html",
        books=data["books"],
        users=data["users"],
        loans=data["loans"],
    )


app.register_blueprint(book_bp)
app.register_blueprint(user_bp)
app.register_blueprint(loan_bp)

if __name__ == "__main__":
    app.run(debug=True)
