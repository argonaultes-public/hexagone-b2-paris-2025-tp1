
class Book:

    def __init__(self, id, author, title, content):
        self.__id = int(id)
        self.__title = title
        self.__author = author
        self.__content = content

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'{self.__id}: {self.__title}'

class BookStore:
    
    def __init__(self):
        self.__books = set()

    def add(self, book):
        self.__books.add(book)

    def delete(self, book_id):
        book_to_remove = self.get(book_id)
        self.__books.remove(book_to_remove)

    def get(self, book_id):
        book_result = None
        for book in self.__books:
            if book.id == book_id:
                book_result = book
                break
        return book_result

    def list(self):
        for book in self.__books:
            print(book)

class Library:
    pass