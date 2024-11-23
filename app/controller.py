import view
import repo


class Controller:
    """Класс слоя контроллера, отвечающий за бизнес логику приложения."""

    def __init__(self, repo: repo.LibraryRepository):
        self.repo = repo


    def add_book(self, title: str, author: str, year: str) -> None:
        self.repo.add_book(title, author, year)


    def delete_book(self, id_: int) -> None:
        self.repo.delete_book(id_)


    def search_book_id(self, id_: int) -> None:
        view.show_book(self.repo.search_book_id(id_))


    def search_book_title(self, title: str) -> None:
        view.show_book(self.repo.search_book_title(title))


    def search_book_author(self, author: str) -> None:
        view.show_book(self.repo.search_book_author(author))


    def show_all_books(self) -> None:
        books = self.repo.get_all_books()
        view.show_books(books)


    def update_status(self, id_: int) -> None:
        self.repo.update_book_status(id_)


library = repo.LibraryRepository('./db.json')

controller = Controller(library)


def main():
    while True:
        view.show_menu()
        try:
            match int(input("Выберите пункт меню: ")):
                case 1:
                    title = input("Название: ")
                    author = input("Автор: ")
                    year = input("Год выпуска: ")
                    controller.add_book(title, author, year)
                    print("Книга добавлена")

                case 2:
                    id_ = int(input("id книги: "))
                    controller.delete_book(id_)
                    print("Книга удалена")

                case 3:
                    view.show_menu_search()
                    match int(input("Выберите пункт меню: ")):
                        case 1:
                            id_ = int(input('id: '))
                            controller.search_book_id(id_)
                        case 2:
                            title = input('название: ')
                            controller.search_book_title(title)
                        case 3:
                            author = input('автор: ')
                            controller.search_book_author(author)
                        case 0:
                            pass
                        case _:
                            print("Неизвестная команда")

                case 4:
                    controller.show_all_books()

                case 5:
                    id_ = int(input("id книги: "))
                    controller.update_status(id_)
                    print("Статус книги изменен")

                case 0:
                    break
                case _:
                    print("Incorrect item")

        except repo.BookNotFoundException:
            print("Книга не найдена")
        except ValueError:
            print("Не корректный ввод")
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    main()