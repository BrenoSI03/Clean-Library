from domain.book import Book
from use_cases.create_book import create_book


def test_criacao_de_livro(mock_book_repo):
    """Deve criar um livro usando o repositório."""

    mock_book_repo.create.return_value = Book(
        id=1, title="Clean Code", author="Robert Martin", available=True
    )

    livro = create_book(mock_book_repo, "Clean Code", "Robert Martin", True)

    assert isinstance(livro, Book), "O retorno deveria ser um objeto Book"
    assert livro.id == 1, "ID do livro deveria ser 1"
    assert livro.title == "Clean Code", "Título incorreto"
    assert livro.author == "Robert Martin", "Autor incorreto"
    assert livro.available is True, "Livro deveria estar disponível"

    mock_book_repo.create.assert_called_once_with("Clean Code", "Robert Martin", True)
