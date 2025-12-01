from domain.book import Book
from repositories.book_repository import BookRepository

def create_book(repo: BookRepository, title: str, author: str, available: bool) -> Book:
    if not title:
        raise ValueError("Título é obrigatório")
    if not author:
        raise ValueError("Autor é obrigatório")
    
    return repo.create(title, author, available)
