#!/usr/bin/python3
"""
    Derived class with inherits from list.
"""


class MyList(list):
    """ MyList class that inherits form list """
    def print_sorted(self):
        """ Prints a sorted list in ascending order """
        if all(isinstance(e, int) for e in self):
            print(sorted(self))
        else:
            raise TypeError("All elements must be integers")
