import json
from unittest.mock import patch

import pytest

from app.model import Book
import app.repo as repo


@pytest.fixture
def temp_repo() -> repo.LibraryRepository:
    """Fixture for temp DB"""
    with open('test_db.json', 'w', encoding='utf-8') as f:
        json.dump([], f)
    temp_repo: repo.LibraryRepository = repo.LibraryRepository('test_db.json')
    return temp_repo


def test_save_book(temp_repo: repo.LibraryRepository):
    temp_repo.books.append(Book(id_=1, title="Test Title", author="Test Author", year="2024"))
    temp_repo._save_book()

    with open(temp_repo.DATABASE, "r") as f:
        data = json.load(f)
    assert data == [{"id_": 1, "title": "Test Title", "author": "Test Author", "year": "2024", "status": "In stock"}]


def test_add_book(temp_repo: repo.LibraryRepository):
    with patch('app.repo.LibraryRepository._save_book') as mock_save:
        temp_repo.add_book("Title", "Author", "1999")

        assert len(temp_repo.books) == 1

        assert temp_repo.books[0].id_ == 1
        assert temp_repo.books[0].title == "Title"
        assert temp_repo.books[0].author == "Author"
        assert temp_repo.books[0].year == "1999"
        assert temp_repo.books[0].status == "In stock"

        mock_save.assert_called_once()


def test_delete_book(temp_repo: repo.LibraryRepository):
    with patch('app.repo.LibraryRepository._save_book') as mock_save:
        temp_repo.books.append(Book(id_=1, title="Test Title", author="Test Author", year="2024"))
        temp_repo.delete_book(1)

        assert len(temp_repo.books) == 0

        mock_save.assert_called()

    with pytest.raises(repo.NotFoundException):
        temp_repo.delete_book(999)


def test_search_book_id(temp_repo: repo.LibraryRepository):
    temp_repo.books.append(Book(id_=1, title="Test Title", author="Test Author", year="2024"))
    book = temp_repo.search_book_id(1)

    assert book.id_ == 1
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.year == "2024"
    assert book.status == "In stock"

    with pytest.raises(repo.NotFoundException):
        temp_repo.search_book_id(999)


def test_search_book_title(temp_repo: repo.LibraryRepository):
    temp_repo.books.append(Book(id_=1, title="Test Title", author="Test Author", year="2024"))
    book = temp_repo.search_book_title("Test Title")

    assert book.id_ == 1
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.year == "2024"
    assert book.status == "In stock"

    with pytest.raises(repo.NotFoundException):
        temp_repo.search_book_title("NOTFOUND")


def test_search_book_author(temp_repo: repo.LibraryRepository):
    temp_repo.books.append(Book(id_=1, title="Test Title", author="Test Author", year="2024"))
    book = temp_repo.search_book_author("Test Author")

    assert book.id_ == 1
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.year == "2024"
    assert book.status == "In stock"

    with pytest.raises(repo.NotFoundException):
        temp_repo.search_book_author("NOTFOUND")


def test_get_all_books(temp_repo: repo.LibraryRepository):
    temp_repo.books.append(Book(id_=1, title="Test Title", author="Test Author", year="2024"))
    temp_repo.books.append(Book(id_=2, title="Test Title", author="Test Author", year="2024"))
    
    assert len(temp_repo.get_all_books()) == 2


def test_update_book_status(temp_repo: repo.LibraryRepository):
    temp_repo.books.append(Book(id_=1, title="Test Title", author="Test Author", year="2024"))

    temp_repo.update_book_status(1)

    assert temp_repo.books[0].status == "Given"
    temp_repo.update_book_status(1)
    assert temp_repo.books[0].status == "In stock"

    with pytest.raises(repo.NotFoundException):
        temp_repo.search_book_author(999)
