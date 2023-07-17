#!/usr/bin/python3
'''Defining a rectangle Class
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Module that represents a square
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializing a Square
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''string represation of square
        '''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        '''size getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updating square class
        '''
        if len(args):
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''display dictonary representation
        '''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
