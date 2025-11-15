from flask import Blueprint, request, jsonify
from use_cases.add_book import AddBookUseCase
from use_cases.list_books import ListBooksUseCase

def create_book_routes(book_repo):

    bp = Blueprint("books", __name__)

    @bp.post("/")
    def add_book():
        data = request.json
        result = AddBookUseCase(book_repo).execute(
            data["title"], data["author"]
        )
        return jsonify({"id": result.id, "title": result.title}), 201

    @bp.get("/")
    def list_books():
        books = ListBooksUseCase(book_repo).execute()
        return jsonify([vars(b) for b in books])

    return bp
