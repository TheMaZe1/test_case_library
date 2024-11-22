import view
import repo


library = repo.LibraryRepository()


def add_book(title: str, author: str, year: str) -> None:
    library.add_book(title, author, year)


def delete_book(id_: int) -> None:
    library.delete_book(id_)


def search_book_id(id_: int) -> None:
    view.show_book(library.search_book_id(id_))


def search_book_title(title: str) -> None:
    view.show_book(library.search_book_id(title))


def search_book_author(author: str) -> None:
    view.show_book(library.search_book_id(author))


def show_all_books() -> None:
    books = library.get_all_books()
    view.show_books(books)


def update_status(id_: int) -> None:
    library.update_book_status(id_)


def main():
    while True:
        view.show_menu()
        try:
            match int(input("Select a menu item: ")):
                case 1:
                    title = input("Title: ")
                    author = input("Author: ")
                    year = input("Year: ")
                    add_book(title, author, year)
                    print("Book added")

                case 2:
                    id_ = int(input("id book: "))
                    delete_book(id_)
                    print("Book not found")

                case 3:
                    view.show_menu_search()
                    match int(input("Select a menu item: ")):
                        case 1:
                            id_ = int(input('id: '))
                            search_book_id(id_)
                        case 2:
                            title = input('title: ')
                            search_book_title(title)
                        case 3:
                            author = input('author: ')
                            search_book_author(author)
                        case 0:
                            pass
                        case _:
                            print("Incorrect item")

                case 4:
                    show_all_books()

                case 5:
                    id_ = int(input("id book: "))
                    update_status(id_)
                    print("Book not found")

                case 0:
                    break
                case _:
                    print("Incorrect item")

        except repo.NotFoundException:
            print("Book not found")
        except ValueError:
            print("Input error")
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    main()