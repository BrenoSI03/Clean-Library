from domain.user import User


def test_criacao_de_usuario_basica():
    usuario = User(id=1, name="Alice")
    assert usuario.id == 1, "ID do usuário deveria ser 1"
    assert usuario.name == "Alice", "Nome do usuário não corresponde ao esperado"


def test_repr_ou_str_do_usuario():
    usuario = User(id=7, name="Bob")
    s = str(usuario)
    r = repr(usuario)
    assert isinstance(s, str), "str(usuario) deveria retornar uma string"
    assert isinstance(r, str), "repr(usuario) deveria retornar uma string"


def test_atualizacao_de_nome_em_memoria():
    """Garante que o atributo name pode ser atualizado (se a entidade não for congelada)."""
    usuario = User(id=2, name="Carol")
    usuario.name = "Carolina"
    assert usuario.name == "Carolina", "Atualização do nome não refletiu no objeto User"
