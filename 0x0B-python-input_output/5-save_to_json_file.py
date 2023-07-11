#!/usr/bin/python3
''' function that writes an object to a text file, using a json representation
'''
import json


def save_to_json_file(my_obj, filename):
    ''' module that accepts Python object
        and sends its json representation to file
    '''
    with open(filename, 'w') as files:
        files.write(json.dumps(my_obj))
