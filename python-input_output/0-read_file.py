#!/usr/bin/python3
"""
    Function that reads a text file.
"""


def read_file(filename=""):
    """ Read file """
    with open(filename, 'r', encoding="utf8") as f:
        for line in f:
            print(line, end="")
