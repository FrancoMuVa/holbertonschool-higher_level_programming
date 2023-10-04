#!/usr/bin/python3
"""
    Derived class with inherits from list.
"""


class MyList(list):
    """ MyList class that inherits form list """
    def print_sorted(self):
        """ Prints a sorted list in ascending order """
        print("{}".format(sorted(self)))
