#!/usr/bin/python3
'''defining the class student'''


class Student:
    '''student class creating'''

    def __init__(self, first_name, last_name, age):
        '''defining initialization method'''
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def to_json(self):
        '''a method that returns dictionary'''

        return self.__dict__
