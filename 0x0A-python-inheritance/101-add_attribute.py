#!/usr/bin/python3
'''Defining a method that adds attributes to objects.'''


def add_attribute(obj, att, value):
    '''Add a new attribute to an object if possible.
    Arguments:
        obj (any): The object to added on it.
        att (str): The name of the attribute to be added.
        value (any): The value of attribute att.
    Raises:
        TypeError: If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
