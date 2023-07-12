#!/usr/bin/python3
'''Defining student class.'''


class Student:
    '''Represent a student.'''

    def __init__(self, first_name, last_name, age):
        '''Initialize a new Student.
        Arguments:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Get a dictionary representation of the Student.
        If attributess is a list of strings, represents only those attributes
        included in the list.
        Arguments:
            attrs (list): (Optional) The attributes to represent.
        '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__
