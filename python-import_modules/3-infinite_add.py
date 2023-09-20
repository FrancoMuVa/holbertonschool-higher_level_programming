#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    add = 0
    for ar in range(1, args):
        add = add + int(argv[ar])
    print("{}".format(add))
