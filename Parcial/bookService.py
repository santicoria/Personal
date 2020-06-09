from book import Book
from repository import Repository


class BookService(Book):
    def create_book(self, name, authorName, memberLegajo):
        name = input('Ingrese nombre: ')
        authorName = input('Ingrese nombre del autor: ')
        memberLegajo = input('Ingrese legajo: ')
        return Book(name, authorName, memberLegajo)

    def add_book(self, book=None):
        if book is None:
            book = self.create_book()
        bookKey = len(Repository.booksList)
        Repository.booksList[bookKey] = book.__dict__

    def update_book(self, bookKey=None, book=None):
        if bookKey is None:
            bookKey = int(input('Ingrese una llave: '))
        if book is None:
            book = self.create_book
        Repository.booksList[bookKey] = book.__dict__

    def delete_book(self, bookKey=None):
        if bookKey is None:
            bookKey = int(input('Ingrese una llave: '))
        del Repository.booksList[bookKey]
