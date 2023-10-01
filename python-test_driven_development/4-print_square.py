#!/usr/bin/python3
"""
    Function that prints a squere with the character '#'
"""


def print_square(size):
    """
        Print a square with a specific size in @size.

        Args:
            size (Int): The size of square.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("{}".format("#" * size))
