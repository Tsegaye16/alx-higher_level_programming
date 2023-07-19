#!/usr/bin/python3
'''
    Rectangle class
'''
class Rectangle(Base):
    '''defining Rectangle class
        that inherited from base
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''print private variable(width)'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set private variable(width)'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(value))
        else:
            self.__width = value

    @property
    def height(self):
        '''
            print private variable(height)
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            set private variable(height)
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(value))
        else:
            self.__height = value

    @property
    def x(self):
        '''
            print private variable(x)
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            set private variable(x)
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(value))
        else:
            self.__x = value

    @property
    def y(self):
        '''print private variable(y)'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set private variable(y)'''
        if not isinstance(value, int):
            raise TypeError( "{} must be an integer".format(value))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(value))
        else:
            self.__y = value

    def area(self):
        '''
            Returns the area of the rectangle
        '''
        return (self.height * self.width)

    def display(self):
        '''
            Prints to stdout the representation of the rectangle
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        '''
            Overwritting the str method
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of a Rectangle
        '''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
