import pytest
from domain.book import Book
from use_cases.update_book import update_book


def test_atualizacao_basica_de_livro(mock_book_repo, mock_loan_repo):
    """Deve atualizar título, autor e disponibilidade quando permitido."""

    livro = Book(1, "A", "X", True)

    mock_book_repo.get_by_id.return_value = livro
    mock_loan_repo.has_any_loan.return_value = False

    livro_atualizado = update_book(
        mock_book_repo, mock_loan_repo,
        book_id=1,
        title="Novo Título",
        author="Novo Autor",
        available=False
    )

    assert livro_atualizado.title == "Novo Título", "Título não foi atualizado"
    assert livro_atualizado.author == "Novo Autor", "Autor não foi atualizado"
    assert livro_atualizado.available is False, "Disponibilidade não atualizada"

    mock_book_repo.update.assert_called_once()


def test_atualizacao_de_livro_emprestado_sem_mudar_disponibilidade(mock_book_repo, mock_loan_repo):
    """Se o livro estiver emprestado, permitir atualizar título/autor, mas NÃO disponibilidade."""

    livro = Book(1, "A", "X", True)

    mock_book_repo.get_by_id.return_value = livro
    mock_loan_repo.has_any_loan.return_value = True   # livro emprestado

    livro_atualizado = update_book(
        mock_book_repo, mock_loan_repo,
        1, "Novo", "Autor Novo", True  # tentar manter True → permitido
    )

    assert livro_atualizado.title == "Novo", "Título deveria ser atualizado"
    assert livro_atualizado.available is True, "Disponibilidade não deveria mudar"


def test_proibir_mudar_disponibilidade_de_livro_emprestado(mock_book_repo, mock_loan_repo):
    """Não pode alterar disponibilidade se o livro está emprestado."""

    livro = Book(1, "A", "X", True)

    mock_book_repo.get_by_id.return_value = livro
    mock_loan_repo.has_any_loan.return_value = True   # livro emprestado

    with pytest.raises(ValueError, match="disponibilidade"):
        update_book(mock_book_repo, mock_loan_repo, 1, "A", "X", False)


def test_livro_inexistente(mock_book_repo, mock_loan_repo):
    """Deve falhar se o livro não existir."""

    mock_book_repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="not found|não encontrado"):
        update_book(mock_book_repo, mock_loan_repo, 99, "X", "Y", True)
