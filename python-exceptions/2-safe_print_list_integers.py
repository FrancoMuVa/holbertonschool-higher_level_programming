#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        printed = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed += 1
        print()
        return printed
    except ValueError:
        print()
        return printed
