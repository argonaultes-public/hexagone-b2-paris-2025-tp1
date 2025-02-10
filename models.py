
class Book:

    def __init__(self, id, author, title, content):
        self.__id = id #TODO: do not expose
        self.__title = title
        self.__author = author
        self.__content = content

class BookStore:
    
    def add(self, book):
        pass

class Library:
    pass