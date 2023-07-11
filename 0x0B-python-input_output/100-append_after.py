#!/usr/bin/python3
'''
Defining module that append_after method.
'''


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting text after search string.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as files:
        lines = files.readlines()
        i = 0
        while n < len(lines):
            if search_string in lines[n]:
                lines[n:n + 1] = [lines[n], new_string]
                n += 1
            n += 1
    with open(filename, "w", encoding="utf-8") as files:
        files.writelines(lines)
