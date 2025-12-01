from domain.book import Book
from use_cases.list_books import list_books


def test_listagem_de_livros(mock_book_repo):
    """Deve retornar a lista de livros do repositório."""

    mock_book_repo.list_all.return_value = [
        Book(id=1, title="A", author="X", available=True),
        Book(id=2, title="B", author="Y", available=False),
    ]

    livros = list_books(mock_book_repo)

    assert len(livros) == 2, "Deveria haver 2 livros na listagem"
    assert livros[0].title == "A", "Título do primeiro livro incorreto"
    assert livros[1].available is False, "Estado de disponibilidade incorreto"

    mock_book_repo.list_all.assert_called_once()
