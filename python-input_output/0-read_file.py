#!/usr/bin/python3
"""
    Function that reads a text file.
"""


def read_file(filename=""):
    """ Read file """
    with open('my_file_0.txt', 'r', encoding="utf=8") as f:
        for line in f:
            print("{}".format(line), end="")
