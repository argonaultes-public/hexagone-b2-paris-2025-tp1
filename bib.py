import json
import jsonpickle

class Livre:

    def __init__(self):
        self.__title = 'title'

class Desktop:

    def __init__(self):
        self.__brand = 'meuble'

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_value):
        if len(new_value) > 3:
            self.__brand = new_value

def process_trucs():
    pass


if __name__ == '__main__':
    d = Desktop()
    print(d.brand)
    d.brand = 'he'
    print(d.brand)
    print(json.dumps({'brand': d.brand}))
    print(jsonpickle.encode(d))
