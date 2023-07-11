#!/usr/bin/python3
'''defining the function that displays
    json representation of string
'''

import json


def to_json_string(my_obj):
    ''' module to_json_string
     returns JSON representation
    '''
    return json.dumps(my_obj)
