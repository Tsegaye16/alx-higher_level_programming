#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *
    counter = len(argv)

    if counter != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    number1 = int(argv[1])
    number2 = int(argv[3])
    op = argv[2]

    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def add_():
        total = add(number1, number2)
        print("{:d} + {:d} = {:d}".format(number1, number2, total))
        return total

    def sub_():
        total = sub(number1, number2)
        print("{:d} - {:d} = {:d}".format(number1, number2, total))
        return total

    def mul_():
        total = mul(number1, number2)
        print("{:d} * {:d} = {:d}".format(number1, number2, total))
        return total

    def div_():
        total = div(number1, number2)
        print("{:d} / {:d} = {:d}".format(number1, number2, total))
        return total

    options = {
        "+": add_,
        "-": sub_,
        "*": mul_,
        "/": div_
    }
    options.get(op, not_found)()
