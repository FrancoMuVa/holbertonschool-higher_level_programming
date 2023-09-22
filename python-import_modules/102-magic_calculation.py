#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    op = argv[2]
    if op == "+":
        resu = add(a, b)
    elif op == "-":
        resu = sub(a, b)
    elif op == "*":
        resu = mul(a, b)
    elif op == "/":
        resu = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, argv[2], b, resu))


dis.dis(magic_calculation)
