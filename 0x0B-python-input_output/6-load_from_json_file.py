#!/usr/bin/python3
'''Defining a function that reads
    json file'''
import json


def load_from_json_file(filename):
    '''Create a Python object from a json file'''
    with open(filename) as files:
        return json.load(files)
