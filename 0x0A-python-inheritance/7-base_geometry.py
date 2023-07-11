#!/usr/bin/python3
"""
This is an empty BaseGeometry class.
"""


class BaseGeometry:
    """ Class: BaseGeometry
    """
    def area(self):
        """unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value to be an int grater than 0.

        Arguments:
            name (str): name of the value
            value (unknown): to be validated.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <=0:
            raise ValueError(("{} must be greater than 0".format(name)
