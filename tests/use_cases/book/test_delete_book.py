import pytest
from domain.book import Book
from use_cases.delete_book import delete_book


def test_delecao_de_livro_sem_emprestimos(mock_book_repo, mock_loan_repo):
    """Deve deletar o livro quando não houver empréstimos."""

    mock_loan_repo.has_any_loan.return_value = False
    mock_book_repo.get_by_id.return_value = Book(1, "A", "X", True)

    delete_book(mock_book_repo, mock_loan_repo, 1)

    mock_book_repo.delete.assert_called_once_with(1)


def test_nao_deletar_livro_emprestado(mock_book_repo, mock_loan_repo):
    """Não deve permitir deletar um livro emprestado."""

    mock_loan_repo.has_any_loan.return_value = True

    with pytest.raises(ValueError, match="emprestado"):
        delete_book(mock_book_repo, mock_loan_repo, 1)


def test_delecao_de_livro_inexistente(mock_book_repo, mock_loan_repo):
    """Não deve deletar livro inexistente."""

    mock_loan_repo.has_any_loan.return_value = False
    mock_book_repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="não encontrado"):
        delete_book(mock_book_repo, mock_loan_repo, 1)
