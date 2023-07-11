#!/usr/bin/python3
''' function that returns the number
    of lines of a text file
'''


def write_file(filename="", text=""):
    ''' function: number_of_lines
    '''
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except IOError:
        print("An error occurred while writing to the file.")
        return 0
