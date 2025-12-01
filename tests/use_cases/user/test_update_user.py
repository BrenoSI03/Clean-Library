import pytest
from use_cases.update_user import update_user
from domain.user import User


def test_atualizacao_de_usuario(mock_user_repo):
    usuario_existente = User(id=1, name="Antigo")
    mock_user_repo.get_by_id.return_value = usuario_existente

    usuario_atualizado = update_user(mock_user_repo, 1, "Novo Nome")

    assert usuario_atualizado.name == "Novo Nome", "O nome do usuário deveria ser atualizado"
    mock_user_repo.update.assert_called_once_with(usuario_existente)


def test_atualizacao_usuario_inexistente(mock_user_repo):
    mock_user_repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="User not found"):
        update_user(mock_user_repo, 999, "Novo Nome")
