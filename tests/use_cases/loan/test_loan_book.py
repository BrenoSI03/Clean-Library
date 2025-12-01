import pytest
from use_cases.loan_book import loan_book
from domain.book import Book
from domain.user import User


def test_emprestimo_com_sucesso(mock_loan_repo, mock_book_repo, mock_user_repo):
    mock_user_repo.get_by_id.return_value = User(id=1, name="Usuário X")
    mock_book_repo.get_by_id.return_value = Book(id=1, title="Teste", author="Autor", available=True)
    mock_loan_repo.has_active_loan.return_value = False
    mock_loan_repo.has_any_loan.return_value = False

    loan_book(mock_loan_repo, mock_book_repo, mock_user_repo, user_id=1, book_id=1)

    mock_loan_repo.borrow_book.assert_called_once_with(1, 1)
    mock_book_repo.update.assert_called_once()

    assert mock_book_repo.update.call_args[0][0].available is False, \
        "Livro deveria ter ficado indisponível após o empréstimo"


def test_emprestimo_usuario_inexistente(mock_loan_repo, mock_book_repo, mock_user_repo):
    mock_user_repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="Usuário não encontrado"):
        loan_book(mock_loan_repo, mock_book_repo, mock_user_repo, 1, 1)


def test_emprestimo_livro_inexistente(mock_loan_repo, mock_book_repo, mock_user_repo):
    mock_user_repo.get_by_id.return_value = User(id=1, name="Teste")
    mock_book_repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="Livro não encontrado"):
        loan_book(mock_loan_repo, mock_book_repo, mock_user_repo, 1, 10)


def test_emprestimo_livro_indisponivel(mock_loan_repo, mock_book_repo, mock_user_repo):
    mock_user_repo.get_by_id.return_value = User(id=1, name="Teste")
    mock_book_repo.get_by_id.return_value = Book(id=1, title="ABC", author="X", available=False)

    with pytest.raises(ValueError, match="indisponível"):
        loan_book(mock_loan_repo, mock_book_repo, mock_user_repo, 1, 1)


def test_emprestimo_livro_ja_pego_pelo_usuario(mock_loan_repo, mock_book_repo, mock_user_repo):
    mock_user_repo.get_by_id.return_value = User(id=1, name="Teste")
    mock_book_repo.get_by_id.return_value = Book(id=1, title="ABC", author="X", available=True)
    mock_loan_repo.has_active_loan.return_value = True

    with pytest.raises(ValueError, match="já possui este livro"):
        loan_book(mock_loan_repo, mock_book_repo, mock_user_repo, 1, 1)


def test_emprestimo_livro_emprestado_para_outro(mock_loan_repo, mock_book_repo, mock_user_repo):
    mock_user_repo.get_by_id.return_value = User(id=1, name="Teste")
    mock_book_repo.get_by_id.return_value = Book(id=1, title="ABC", author="X", available=True)
    mock_loan_repo.has_active_loan.return_value = False
    mock_loan_repo.has_any_loan.return_value = True

    with pytest.raises(ValueError, match="emprestado"):
        loan_book(mock_loan_repo, mock_book_repo, mock_user_repo, 1, 1)
