#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
