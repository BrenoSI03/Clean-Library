from unittest.mock import Mock
from app.use_cases.create_book import create_book
from domain.book import Book

def test_create_book_calls_repo():
    repo = Mock()
    repo.create.return_value = Book(id=1, title="1984", author="Orwell", available=True)

    result = create_book(repo, "1984", "Orwell", True)

    repo.create.assert_called_once_with("1984", "Orwell", True)
    assert result.id == 1
