#!/usr/bin/python3
"""
defining module to check inherit from
"""


def inherits_from(obj, a_class):
    """Method for comparing object classes

    Arguments:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.

    Return:
        True if obj isinstance of a_class/ class that inherits from it.
        otherwise False

    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
