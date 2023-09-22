#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a > b:
        c = add(a, b)
        return c
    else:
        c = sub(a, b)
        return c


dis.dis(magic_calculation)
