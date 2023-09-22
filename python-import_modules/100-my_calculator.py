#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    op = argv[2]
    if op == "+":
        resu = a + b
    elif op == "-":
        resu = a - b
    elif op == "*":
        resu = a * b
    elif op == "/":
        resu = a / b
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, argv[2], b, resu))
