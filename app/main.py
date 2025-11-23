from flask import Flask
from routes.book_routes import book_bp
from routes.user_routes import user_bp

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = "grXBaIz0Ag0a7XllLUI3maScR7mbnFZC"

    app.register_blueprint(book_bp)
    app.register_blueprint(user_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
