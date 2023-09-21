#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_a = tuple_a[0:2] + (0, 0)
    new_b = tuple_b[0:2] + (0, 0)

    new_tuple = (new_a[0] + new_b[0], new_a[1] + new_b[1])
    return new_tuple
