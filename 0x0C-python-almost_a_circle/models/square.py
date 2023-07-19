#!/usr/bin/python3
'''defining Rectangle class
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    representing Square module
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialising a Square class
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''module string represation of square
        '''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        '''module Square size getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''setting the value
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Assigns attributes based on the provided
        arguments: id, size, x, y
        '''
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of a Square
        '''
        return {     
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
