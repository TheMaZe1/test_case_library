from dataclasses import asdict
import os
import copy
import json

from model import Book


class BookNotFoundException(Exception):
    pass


class LibraryRepository:
    """Класс слоя репозитория, для взаимодействия с БД."""

    STATUS = {
        'In stock': 'Given',
        'Given': 'In stock'
    }

    def __init__(self, database_path: str) -> None:
        self.books: list[Book] = []
        self.DATABASE = database_path
        if os.path.exists(self.DATABASE):
            with open(self.DATABASE, 'r', encoding='UTF-8') as f:
                books: list[dict] = json.load(f)
                for book in books:
                    self.books.append(Book(int(book['id_']) ,book['title'],book['author'],book['year'],book['status']))


    def add_book(self, title: str, author: str, year: str) -> None:
        """Добавить книгу в БД.
        ID задается последовательно, ID последней книги + 1.
        """
        if self.books:
            id_: int = self.books[-1].id_ + 1
        else:
            id_: int = 1
        
        book: Book = Book(id_, title, author, year)
        self.books.append(book)

        self._save_book()


    def delete_book(self, id_: int) -> None:
        """Удаляет книгу по указаному id. Бросает исключение если книга не найдена.
        Удаляет первую подходящую книгу.
        """
        result: Book | None = next((book for book in self.books if book.id_ == id_), None)
        if result:
            self.books.remove(result)
            self._save_book()
        else:
            raise BookNotFoundException
        

    def search_book_id(self, id_: int) -> Book:
        """Ищет книгу по указаному id. Бросает исключение если книга не найдена.
        """
        result: Book | None = next((book for book in self.books if book.id_ == id_), None)
        if result:
            return result
        else:
            raise BookNotFoundException


    def search_book_title(self, title: str) -> Book:
        """Ищет книгу по указаному title. Бросает исключение если книга не найдена.
        Возвращает первую подходящую книгу.
        """
        result: Book | None = next((book for book in self.books if book.title == title), None)
        if result:
            return result
        else:
            raise BookNotFoundException

    def search_book_author(self, author: str) -> Book:
        """Ищет книгу по указаному автору. Бросает исключение если книга не найдена.
        Возвращает первую подходящую книгу.
        """
        result: Book | None = next((book for book in self.books if book.author == author), None)
        if result:
            return result
        else:
            raise BookNotFoundException


    def get_all_books(self) -> list[Book]:
        """Возвращает список книг.
        Возвращается глубокая копия списка книг, для невозможности изменения из вне.
        """
        return copy.deepcopy(self.books)

    
    def update_book_status(self, id_: int) -> None:
        """Изменяет статус книги.
        "In stock" -> "Given",
        "Given" -> "In stock".
        """
        result: Book | None = next((book for book in self.books if book.id_ == id_), None)
        if result:
            result.status = self.STATUS[result.status]
            self._save_book()
        else:
            raise BookNotFoundException


    def _save_book(self) -> None:
        """Сохранени изменений в БД(JSON файл).
        Не эффективный способ, так как файл каждый раз переписываеться целиком.
        """
        with open(self.DATABASE, 'w') as f:
            f.write(json.dumps([asdict(book) for book in self.books]))