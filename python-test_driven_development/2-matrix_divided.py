#!/usr/bin/python3
"""
    Function that divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of matrix by a given number.

        Args:
            matrix (list of list): The matrix.
            div (int or float): The divisor.

        Return: Returns a new matrix (list of list).
    """
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
