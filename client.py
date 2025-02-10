class Client:

    def __init__(self):
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book,
        'd': self.delete_book,
        'g': self.get_book,
        's': self.save_to_disk,
        'q': self.should_continue
        }


    def should_continue(self):
        return False

    def list_books(self):
        #TODO: list from server
        return True

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')
        #TODO: send to the server
        return True

    def delete_book(self):
        book_id = int(input('Book id: '))
        #TODO: send to the server
        return True

    def get_book(self):
        book_id = input('Book id: ')
        book = None
        #TODO: get book from the server
        print(book)
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
    client = Client()
    client.run()