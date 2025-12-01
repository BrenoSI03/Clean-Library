from use_cases.list_user_loans import list_books_for_user


def test_listagem_livros_usuario(mock_loan_repo):
    mock_loan_repo.list_books_for_user.return_value = [
        {"id": 1, "title": "Livro A", "author": "Autor X"},
        {"id": 2, "title": "Livro B", "author": "Autor Y"},
    ]

    resultado = list_books_for_user(mock_loan_repo, user_id=10)

    assert len(resultado) == 2, "Deveria retornar dois livros emprestados"
    assert resultado[0]["title"] == "Livro A", "O título do primeiro livro está incorreto"
    assert resultado[1]["author"] == "Autor Y", "O autor do segundo livro está incorreto"

    mock_loan_repo.list_books_for_user.assert_called_once_with(10)
