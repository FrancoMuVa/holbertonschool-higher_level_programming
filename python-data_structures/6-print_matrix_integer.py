#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    leng_i = len(matrix)
    for i in range(0, leng_i):
        leng_j = len(matrix[i])
        for j in range(0, leng_j):
            print("{:d}".format(matrix[i][j]), end="")
            if j != leng_j:
                print(" ", end="")
        print()
