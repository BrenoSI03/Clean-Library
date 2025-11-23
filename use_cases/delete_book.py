from repositories.book_repository import BookRepository

def delete_book(repo: BookRepository, book_id: int) -> None:
    book = repo.get_by_id(book_id)
    if book is None:
        raise ValueError("Livro não encontrado")

    repo.delete(book_id)
