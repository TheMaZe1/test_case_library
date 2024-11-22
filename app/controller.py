import view
import repo


library = repo.LibraryRepository('./db.json')


def add_book(title: str, author: str, year: str, repo: repo.LibraryRepository) -> None:
    repo.add_book(title, author, year)


def delete_book(id_: int, repo: repo.LibraryRepository) -> None:
    repo.delete_book(id_)


def search_book_id(id_: int, repo: repo.LibraryRepository) -> None:
    view.show_book(repo.search_book_id(id_))


def search_book_title(title: str, repo: repo.LibraryRepository) -> None:
    view.show_book(repo.search_book_title(title))


def search_book_author(author: str, repo: repo.LibraryRepository) -> None:
    view.show_book(repo.search_book_author(author))


def show_all_books(repo: repo.LibraryRepository) -> None:
    books = repo.get_all_books()
    view.show_books(books)


def update_status(id_: int, repo: repo.LibraryRepository) -> None:
    repo.update_book_status(id_)


def main():
    while True:
        view.show_menu()
        try:
            match int(input("Select a menu item: ")):
                case 1:
                    title = input("Title: ")
                    author = input("Author: ")
                    year = input("Year: ")
                    add_book(title, author, year, library)
                    print("Book added")

                case 2:
                    id_ = int(input("id book: "))
                    delete_book(id_, library)
                    print("Book not found")

                case 3:
                    view.show_menu_search()
                    match int(input("Select a menu item: ")):
                        case 1:
                            id_ = int(input('id: '))
                            search_book_id(id_, library)
                        case 2:
                            title = input('title: ')
                            search_book_title(title, library)
                        case 3:
                            author = input('author: ')
                            search_book_author(author, library)
                        case 0:
                            pass
                        case _:
                            print("Incorrect item")

                case 4:
                    show_all_books(library)

                case 5:
                    id_ = int(input("id book: "))
                    update_status(id_, library)
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