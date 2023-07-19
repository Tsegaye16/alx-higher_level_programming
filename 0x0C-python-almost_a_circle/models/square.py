#!/usr/bin/python3
'''defining square class
'''
from modules.rectangle import Rectangle


class Square(Rectangle):
    """module of square
    """

    def __init__(self, size, x=0, y=0, id=None):
        '''initialising a square module
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''detting the size of square
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''setting the size of square
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''string representation of square class
        '''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        '''updating square module
        '''
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''display dictonary
        '''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
