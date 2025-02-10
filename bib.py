import jsonpickle
from models import Book, BookStore, Library

class User:
    pass

class App:

    def __init__(self):
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book,
        'd': self.delete_book,
        'g': self.get_book,
        's': self.save_to_disk,
        'q': self.should_continue
        }
        self.__book_store = BookStore()
        self.__library = Library()
        self.__next_id = 0

    def should_continue(self):
        return False

    def list_books(self):
        self.__book_store.list()
        return True

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')
        book = Book(self.__next_id, author, title, content)
        self.__book_store.add(book)
        self.__next_id += 1
        return True

    def delete_book(self):
        book_id = int(input('Book id: '))
        self.__book_store.delete(book_id)
        return True

    def get_book(self):
        book_id = input('Book id: ')
        book = self.__book_store.get(book_id)
        print(book)
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
            if action in self.__actions:
                should_continue = self.__actions[action]()
            else:
                print(f'Action not supported {action}')

if __name__ == '__main__':
    app = App()
    app.run()
    
