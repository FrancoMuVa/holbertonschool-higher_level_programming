#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    print("{} arguments:".format(args - 1))
    for ar in range(1, args):
        print("{}: {}".format(ar, sys.argv[ar]))
