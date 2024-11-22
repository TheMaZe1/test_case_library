from dataclasses import asdict
import os
import copy
import json

from model import Book


DATABASE = './db.json'

class NotFoundException(Exception):
    pass


class LibraryRepository:

    STATUS = {
        'In stock': 'Given',
        'Given': 'In stock'
    }

    def __init__(self) -> None:
        self.books: list[Book] = []
        if os.path.exists(DATABASE):
            with open(DATABASE, 'r', encoding='UTF-8') as f:
                books: list[dict] = json.load(f)
                for book in books:
                    self.books.append(Book(int(book['id_']) ,book['title'],book['author'],book['year'],book['status']))


    def add_book(self, title: str, author: str, year: str) -> None:
        """Added book to DB"""
        if self.books:
            id_: int = self.books[-1].id_ + 1
        else:
            id_: int = 1
        
        book: Book = Book(id_, title, author, year)
        self.books.append(book)

        self._save_book()


    def delete_book(self, id_: int) -> None:
        """Delete book from DB. Raise exception if book not found"""
        result: Book | None = next((book for book in self.books if book.id_ == id_), None)
        if result:
            self.books.remove(result)
            self._save_book()
        else:
            raise NotFoundException
        

    def search_book_id(self, id_: int) -> Book:
        """Search bok for id. Raise exception if book not found"""
        result: Book = next((book for book in self.books if book.id_ == id_), None)
        if result:
            return result
        else:
            raise NotFoundException


    def search_book_title(self, title: str) -> Book:
        """Search book for titile. Raise exception if book not found"""
        result: Book = next((book for book in self.books if book.title == title), None)
        if result:
            return result
        else:
            raise NotFoundException

    def search_book_author(self, author: str) -> Book:
        """Search book for author. Raise exception if book not found"""
        result: Book = next((book for book in self.books if book.id_ == author), None)
        if result:
            return result
        else:
            raise NotFoundException


    def get_all_books(self) -> list[Book]:
        """Return list of books"""
        return copy.deepcopy(self.books)

    
    def update_book_status(self, id_: int) -> None:
        """Update status for book by id"""
        result: Book = next((book for book in self.books if book.id_ == id_), None)
        if result:
            result.status = self.STATUS[result.status]
            self._save_book()
        else:
            raise NotFoundException


    def _save_book(self) -> None:
        """Inner func, update JSON file DB"""
        with open(DATABASE, 'w') as f:
            f.write(json.dumps([asdict(book) for book in self.books]))