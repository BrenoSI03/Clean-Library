from use_cases.list_users import list_users
from domain.user import User


def test_listagem_de_usuarios(mock_user_repo):
    mock_user_repo.list_all.return_value = [
        User(id=1, name="Alice"),
        User(id=2, name="Bob"),
    ]

    usuarios = list_users(mock_user_repo)

    assert len(usuarios) == 2, "A listagem deveria conter dois usuários"
    assert usuarios[0].name == "Alice", "O primeiro usuário deveria ser 'Alice'"
    assert usuarios[1].name == "Bob", "O segundo usuário deveria ser 'Bob'"

    mock_user_repo.list_all.assert_called_once()
