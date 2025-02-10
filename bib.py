import json
import jsonpickle

class Book:

    def __init__(self, id, author, title, content):
        self.__id = id #TODO: do not expose
        self.__title = title
        self.__author = author
        self.__content = content

class BookStore:
    pass

class Library:
    pass

class User:
    pass

class App:

    def __init__(self):
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book
        }
        self.__book_store = BookStore()


    def list_books(self):
        print('book_store.list()')

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')
        book = Book(0, author, title, content)
        self.__book_store.add(book)


    def run(self):
        action = input('Action? ')
        print(self.__actions[action]())

if __name__ == '__main__':
    app = App()
    app.run()
    
