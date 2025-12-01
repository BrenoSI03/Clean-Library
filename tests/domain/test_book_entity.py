import pytest
from domain.book import Book


def test_criacao_de_livro_basica():
    livro = Book(id=1, title="Clean Code", author="Robert C. Martin", available=True)

    assert livro.id == 1, "ID do livro deveria ser 1"
    assert livro.title == "Clean Code", "Título do livro não corresponde ao esperado"
    assert livro.author == "Robert C. Martin", "Autor do livro não corresponde ao esperado"
    assert livro.available is True, "Livro deveria estar disponível (True)"


@pytest.mark.parametrize("disponivel", [True, False])
def test_livro_parametrizado_disponibilidade(disponivel):
    livro = Book(id=10, title="Duna", author="Frank Herbert", available=disponivel)
    assert livro.available is disponivel, "Estado de disponibilidade não foi armazenado corretamente"


def test_repr_ou_str_do_livro():
    """Não exigimos um formato específico, apenas que __repr__/__str__ existam e sejam strings."""
    livro = Book(id=2, title="Refactoring", author="Martin Fowler", available=False)
    s = str(livro)
    r = repr(livro)
    assert isinstance(s, str), "str(livro) deveria retornar uma string"
    assert isinstance(r, str), "repr(livro) deveria retornar uma string"


def test_alteracao_de_disponibilidade_em_memoria():
    """Confere que a entidade permite atualizar o atributo available em memória (sem persistência)."""
    livro = Book(id=3, title="The Pragmatic Programmer", author="Andy Hunt", available=True)
    livro.available = False
    assert livro.available is False, "Atualização de disponibilidade não refletiu no objeto Book"
