#!/usr/bin/python3
"""
    Append write
"""


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file """
    with open(filename, "a", encoding="UTF8") as f:
        chars = f.write(text)
        return chars
