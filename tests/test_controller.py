from collections.abc import Generator
from unittest.mock import MagicMock, patch
import pytest

from app.controller import Controller


@pytest.fixture
def mock_repo() -> MagicMock:
    """Создание мок-объекта для репозитория"""
    mock_repo: MagicMock = MagicMock()
    return mock_repo


@pytest.fixture
def temp_controller(mock_repo: MagicMock) -> Controller:
    """Создание временного объекта контроллера"""
    temp_controller: Controller = Controller(mock_repo)
    return temp_controller


@pytest.fixture
def mock_view() -> Generator[MagicMock, None, None]:
    """Создание мок-объекта для слоя view"""
    with patch('app.controller.view') as mock_view:
        yield mock_view


def test_add_book(temp_controller: Controller, mock_repo: MagicMock):
    temp_controller.add_book("Test Title", "Test Author", "2024")

    mock_repo.add_book.assert_called_once_with("Test Title", "Test Author", "2024")


def test_delete_book(temp_controller: Controller, mock_repo: MagicMock):
    temp_controller.delete_book(1)

    mock_repo.delete_book.assert_called_once_with(1)


def test_search_book_id(temp_controller: Controller, mock_view: MagicMock, mock_repo: MagicMock):
    temp_controller.search_book_id(1)

    mock_repo.search_book_id.assert_called_once_with(1)
    mock_view.show_book.assert_called_once()


def test_search_book_title(temp_controller: Controller, mock_view: MagicMock, mock_repo: MagicMock):
    temp_controller.search_book_title("Test Title")

    mock_repo.search_book_title.assert_called_once_with("Test Title")
    mock_view.show_book.assert_called_once()


def test_search_book_author(temp_controller: Controller, mock_view: MagicMock, mock_repo: MagicMock):
    temp_controller.search_book_author("Test author")

    mock_repo.search_book_author.assert_called_once_with("Test author")
    mock_view.show_book.assert_called_once()


def test_show_all_books(temp_controller: Controller, mock_view: MagicMock, mock_repo: MagicMock):
    temp_controller.show_all_books()

    mock_repo.get_all_books.assert_called_once()
    mock_view.show_books.assert_called_once()


def test_update_status(temp_controller: Controller, mock_repo: MagicMock):
    temp_controller.update_status(1)

    mock_repo.update_book_status.assert_called_once_with(1)