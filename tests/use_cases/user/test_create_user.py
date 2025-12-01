from use_cases.create_user import create_user
from domain.user import User


def test_criacao_de_usuario(mock_user_repo):
    mock_user_repo.create.return_value = User(id=1, name="Alice")

    usuario = create_user(mock_user_repo, "Alice")

    assert usuario.id == 1, "ID do usuário deveria ser 1"
    assert usuario.name == "Alice", "Nome do usuário deveria ser 'Alice'"

    mock_user_repo.create.assert_called_once_with("Alice")
