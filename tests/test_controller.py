from collections.abc import Generator
from unittest.mock import MagicMock, patch
import pytest

import app.controller as controller


@pytest.fixture
def mock_repo() -> MagicMock:
    """Create mock object for repository"""
    mock_repo: MagicMock = MagicMock()
    return mock_repo

@pytest.fixture
def mock_view() -> Generator[MagicMock, None, None]:
    """Create mock object for view"""
    with patch('app.controller.view') as mock_view:
        yield mock_view


def test_add_book(mock_repo: MagicMock):
    controller.add_book("Test Title", "Test Author", "2024", mock_repo)

    mock_repo.add_book.assert_called_once_with("Test Title", "Test Author", "2024")


def test_delete_book(mock_repo: MagicMock):
    controller.delete_book(1, mock_repo)

    mock_repo.delete_book.assert_called_once_with(1)


def test_search_book_id(mock_repo: MagicMock, mock_view: MagicMock):
    controller.search_book_id(1, mock_repo)

    mock_repo.search_book_id.assert_called_once_with(1)
    mock_view.show_book.assert_called_once()


def test_search_book_title(mock_repo: MagicMock, mock_view: MagicMock):
    controller.search_book_title("Test Title", mock_repo)

    mock_repo.search_book_title.assert_called_once_with("Test Title")
    mock_view.show_book.assert_called_once()


def test_search_book_author(mock_repo: MagicMock, mock_view: MagicMock):
    controller.search_book_author("Test author", mock_repo)

    mock_repo.search_book_author.assert_called_once_with("Test author")
    mock_view.show_book.assert_called_once()


def test_show_all_books(mock_repo: MagicMock, mock_view: MagicMock):
    controller.show_all_books(mock_repo)

    mock_repo.get_all_books.assert_called_once()
    mock_view.show_books.assert_called_once()


def test_update_status(mock_repo: MagicMock):
    controller.update_status(1, mock_repo)

    mock_repo.update_book_status.assert_called_once_with(1)