import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_book_repo():
    """Mock do repositório de livros."""
    return MagicMock()

@pytest.fixture
def mock_loan_repo():
    """Mock do repositório de empréstimos."""
    return MagicMock()

@pytest.fixture
def mock_user_repo():
    """Mock do repositório de usuários."""
    return MagicMock()