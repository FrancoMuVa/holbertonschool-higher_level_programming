#!/usr/bin/python3
def print_last_digit(number):
    num = str(number)[-1]
    print("{}".format(int(num)), end="")
    return (int(num))
