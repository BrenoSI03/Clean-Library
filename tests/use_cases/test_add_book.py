from use_cases.add_book import AddBookUseCase
from domain.entities.book import Book
from unittest.mock import Mock

def test_add_book_use_case():
    repo = Mock()
    repo.add.return_value = Book(1, "Clean Code", "Robert Martin")

    use_case = AddBookUseCase(repo)
    result = use_case.execute("Clean Code", "Robert Martin")

    assert result.id == 1
    repo.add.assert_called_once()
