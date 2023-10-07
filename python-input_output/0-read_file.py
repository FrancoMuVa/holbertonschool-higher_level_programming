#!/usr/bin/python3
"""
    Function that reads a text file.
"""


def read_file(filename=""):
    """ Read file """
    with open('my_file_0.txt', 'r', encoding="utf8") as f:
        read_f = f.read()
        for line in read_f:
            print(line, end="")
        f.close()