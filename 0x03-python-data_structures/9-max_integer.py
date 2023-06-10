#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    maximum_number = my_list[0]
    for number in my_list:
        if number > maximum_number:
            maximum_number = number
    return maximum_number
