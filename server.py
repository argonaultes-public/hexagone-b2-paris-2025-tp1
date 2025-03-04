import jsonpickle
import socketserver
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
        self.__reload_from_disk()
        self.__next_id = self.__book_store.size()
        self.__library = Library()

    def should_continue(self, params = None):
        return False

    def list_books(self, params = None):
        return self.__book_store.list()

    def new_book(self, params):
        author, title, content = params.split(',')
        book = Book(self.__next_id, author, title, content)
        self.__book_store.add(book)
        self.__next_id += 1
        return book

    def delete_book(self, book_id):
        self.__book_store.delete(book_id)
        return book_id

    def get_book(self, book_id):
        return self.__book_store.get(book_id)

    def save_to_disk(self):
        # unpacking
        for filename, obj in [('my_lib.json', self.__library), ('my_book_store.json', self.__book_store)]:
            with open(filename, 'w') as lib_file:
                raw_json = jsonpickle.encode(obj)
                lib_file.write(raw_json)
        return True

    def __reload_from_disk(self):
        with open('my_book_store.json', "r+") as f:
            written_instance = f.read()
            self.__book_store = jsonpickle.decode(written_instance)

    def run(self, action, params):
        return self.__actions[action](params)
    


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        pieces = [b'']
        total = 0
        while b'\n' not in pieces[-1] and total < 10_000:
            pieces.append(self.request.recv(2000))
            total += len(pieces[-1])
        self.data = b''.join(pieces)
        print(f"Received from {self.client_address[0]}:")
        request = self.data.decode("utf-8")
        print(f'request: {request}')
        request_split = request.split(',')
        # message format: action,params
        app = App()
        response = app.run(request_split[0].strip(), ','.join(request_split[1:]))
        # just send back the same data, but upper-cased
        self.request.sendall(str(response).encode(encoding='utf-8'))
        # after we return, the socket will be closed.
        app.save_to_disk()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()