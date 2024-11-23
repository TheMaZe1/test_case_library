from model import Book

def show_menu():
    print('-' * 20)
    print('1. Добавить книгу')
    print('2. Удалить книгу')
    print('3. Найти книгу')
    print('4. Показать книги')
    print('5. Изменить статус книги')
    print('0. Выйти из программы')
    print('-' * 20)


def show_books(books: list[Book]) -> None:
    for book in books:
        print(book)


def show_book(book: Book) -> None:
    print(book)


def show_menu_search():
    print('-' * 20)
    print('1. Найти по id')
    print('2. Найти по названию')
    print('3. Найти по автору')
    print('0. Назад')
    print('-' * 20)