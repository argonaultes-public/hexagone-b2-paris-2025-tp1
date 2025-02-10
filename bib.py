import jsonpickle
from models import Book, BookStore, Library

class User:
    pass

class App:

    def __init__(self):
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book,
        'q': self.should_continue
        }
        self.__book_store = BookStore()
        self.__library = Library()

    def should_continue(self):
        return False

    def list_books(self):
        print('book_store.list()')
        return True

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')
        book = Book(0, author, title, content)
        self.__book_store.add(book)
        return True

    def delete_book(self):
        return True

    def get_book(self):
        return True

    def save_to_disk(self):
        # unpacking

        for filename, obj in [('my_lib.json', self.__library), ('my_book_store.json', self.__book_store)]:
            with open(filename, 'w') as lib_file:
                raw_json = jsonpickle.encode(obj)
                lib_file.write(raw_json)
        return True

    def run(self):
        should_continue = True
        while should_continue:
            action = input('Action? ')
            should_continue = self.__actions[action]()

if __name__ == '__main__':
    app = App()
    app.run()
    
