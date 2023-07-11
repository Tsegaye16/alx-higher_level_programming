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
        """
            Arguments:
            name (str): name of the value
            value (unknown): to be validated.

            this method raise two error:
            1: TypeError, if type of value is not integer
            2: ValueError, if actual value of value is
                less than or equal to 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <=0:
            raise ValueError(("{} must be greater than 0".format(name)
