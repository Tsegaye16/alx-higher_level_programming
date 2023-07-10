#!/usr/bin/python3
"""defining my_list.py module"""


class MyList(list):
    """take list as argument"""
    def print_sorted(self):
        """ return the sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
