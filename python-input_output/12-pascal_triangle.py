#!/usr/bin/python3
"""
    Pascal triangle.
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing
        the Pascal's triangle of n
    """
    pas_trian = []
    if n <= 0:
        return pas_trian

    for level in range(n):
        row = [1]
        if pas_trian:
            r_l = pas_trian[-1]
            row.extend([r_l[j] + r_l[j + 1] for j in range(len(r_l) - 1)])
            row.append(1)
        pas_trian.append(row)
    return pas_trian
