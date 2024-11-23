# Система управления библиотекой

Данное приложение позволяет добавлять, удалять, искать и отображать книги. А также изменять статус книги между "В наличии" и "Выдана"

### Описание функционала

Книга содержит поля:
 - id: идентификатор книги
 - title: название книги
 - author: автор книги
 - year: год выпуска книги
 - status: статус книги("В наличии" или "Выдана")

**Добавление книги:** пользователь вводит название, автора и год выпуска книги, книга добавляется в библиотеку, со сгенерированым id и статусом "In stock".  
**Удаление книги:** пользователь вводит id книги, книга удаляется из библиотеки.  
**Поиск книги:** пользователь может искать книгу по id, нзаванию или автору книги.  
**Отображение всех книг:** программа выводит список всех книг со всеми полями.  
**Изменение статуса книги:** пользователь вводит id книги ее статус меняется с "В наличии" на "Выдана" и наооборот соответствено.  

### Усиановка зависимостей

```bash
pip install -r requirements.txt
```
P.S. По условию задания нельзя использовать сторонние библиотеки. В зависимостях только pytest для написания тестов.

### Использование

Для запуска приложения используйте
```bash
python app\controller.py
```

### Для запуска тестов

```bash
python -m pytest
```