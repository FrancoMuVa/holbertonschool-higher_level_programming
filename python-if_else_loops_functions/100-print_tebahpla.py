#!/usr/bin/python3
for num in reversed(range(97, 123)):
    if num % 2 != 0:
        print("{}".format(chr(num - 32)), end="")
    else:
        print("{}".format(chr(num)), end="")
