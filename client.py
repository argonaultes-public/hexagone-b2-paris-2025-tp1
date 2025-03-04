import socket

class Client:

    def __init__(self):
        self.__host, self.__port = "localhost", 9999
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book,
        'd': self.delete_book,
        'g': self.get_book,
        'q': self.should_continue
        }


    def should_continue(self):
        return False

    def list_books(self):
        return 'ls'

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')

        return f'new,{author},{title},{content}'

    def delete_book(self):
        book_id = int(input('Book id: '))
        return f'd,{book_id}'

    def get_book(self):
        book_id = input('Book id: ')
        return f'g,{book_id}'

    def __send(self, message):
        received = None
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((self.__host, self.__port))
            sock.sendall(bytes(message, "utf-8"))
            sock.sendall(b"\n")

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
        return received

    def run(self):
        should_continue = True
        while should_continue:
            action = input('Action? ')
            if action in self.__actions:
                message = self.__actions[action]()
                response = self.__send(message)
                print(response)
            else:
                print(f'Action not supported {action}')

if __name__ == '__main__':
    client = Client()
    client.run()