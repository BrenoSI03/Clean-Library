import pytest
from use_cases.return_book import return_book
from domain.book import Book


def test_devolucao_com_sucesso(mock_loan_repo, mock_book_repo):
    mock_loan_repo.has_active_loan.return_value = True
    mock_book_repo.get_by_id.return_value = Book(id=1, title="ABC", author="X", available=False)

    return_book(mock_loan_repo, mock_book_repo, user_id=1, book_id=1)

    mock_loan_repo.return_book.assert_called_once_with(1, 1)
    mock_book_repo.update.assert_called_once()

    livro_atualizado = mock_book_repo.update.call_args[0][0]
    assert livro_atualizado.available == 1, "Livro deveria ser marcado como disponível"


def test_devolucao_livro_nao_emprestado(mock_loan_repo, mock_book_repo):
    mock_loan_repo.has_active_loan.return_value = False

    with pytest.raises(ValueError, match="não está emprestado"):
        return_book(mock_loan_repo, mock_book_repo, 1, 1)


def test_devolucao_livro_inexistente(mock_loan_repo, mock_book_repo):
    mock_loan_repo.has_active_loan.return_value = True
    mock_book_repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="Livro não encontrado"):
        return_book(mock_loan_repo, mock_book_repo, 1, 1)
