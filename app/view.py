from model import Book

def show_menu():
    print('-' * 20)
    print('1. Add book')
    print('2. Delete book')
    print('3. Search book')
    print('4. Show books')
    print('5. Switch book status')
    print('0. Exit program')
    print('-' * 20)


def show_books(books: list[Book]) -> None:
    for book in books:
        print(book)


def show_book(book: Book) -> None:
    print(book)


def show_menu_search():
    print('-' * 20)
    print('1. Search by id')
    print('2. Search by title')
    print('3. Search by author')
    print('0. Back')
    print('-' * 20)