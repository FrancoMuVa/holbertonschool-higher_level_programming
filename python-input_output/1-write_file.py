#!/usr/bin/python3
"""
    Write file
"""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file

        Returns: Number of characters written.
    """
    with open(filename, 'w', encoding="UTF8") as f:
        chars = f.write(text)
        return chars
