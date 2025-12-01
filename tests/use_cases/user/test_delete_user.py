import pytest
from use_cases.delete_user import delete_user
from domain.user import User


def test_deletar_usuario_sem_emprestimos(mock_user_repo, mock_loan_repo):
    mock_user_repo.get_by_id.return_value = User(id=1, name="Alice")
    mock_loan_repo.get_loans_by_user.return_value = []

    delete_user(mock_user_repo, mock_loan_repo, 1)

    mock_user_repo.delete.assert_called_once_with(1)


def test_deletar_usuario_inexistente(mock_user_repo, mock_loan_repo):
    mock_user_repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="Usuário não encontrado"):
        delete_user(mock_user_repo, mock_loan_repo, 10)


def test_deletar_usuario_com_emprestimos(mock_user_repo, mock_loan_repo):
    mock_user_repo.get_by_id.return_value = User(id=1, name="Alice")
    mock_loan_repo.get_loans_by_user.return_value = [{"book_id": 2}]

    with pytest.raises(ValueError, match="Não é permitido deletar"):
        delete_user(mock_user_repo, mock_loan_repo, 1)
