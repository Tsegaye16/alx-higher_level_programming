#!/usr/bin/python3
"""defining the function that reads a file """


def read_file(filename=""):
    """reads the txt file (UTF-8) and
        print it in stdout
    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
