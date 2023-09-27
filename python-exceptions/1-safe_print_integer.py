#!/usr/bin/python3
def safe_print_integer(value):
    try:
        isint = False
        if isinstance(value, int):
            isint = True
        print("{:d}".format(value))
        return isint
    except (TypeError, ValueError):
        return isint
