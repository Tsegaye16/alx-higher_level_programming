#!/usr/bin/python3
'''Defining a file-appending method.'''


def append_write(filename="", text=""):
    '''Appends a string to the end of a UTF8 text file.
    Arguments:
        filename (str): The file appending performed on.
        text (str): The string to be append.
    Returns:
        The number of characters appended.
    '''
    with open(filename, "a", encoding="utf-8") as files:
        return files.write(text)
