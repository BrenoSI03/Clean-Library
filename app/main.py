from flask import Flask, redirect, url_for
from app.routes.book_routes import book_bp
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = "grXBaIz0Ag0a7XllLUI3maScR7mbnFZC"

    app.register_blueprint(book_bp)
    app.register_blueprint(user_bp)

    # Rota principal (home) que redireciona para a página de livros
    @app.route('/')
    def home():
        return redirect(url_for('books.home'))  # Redireciona para a página de livros

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
