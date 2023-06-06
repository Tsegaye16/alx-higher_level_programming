#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string
    else:
        return string[:n] + string[n+1:]
