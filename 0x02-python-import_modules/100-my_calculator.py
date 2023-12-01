#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    op = sys.argv[2]
    op_ = ['+', '-', '*', '/']
    if op == op_[0]:
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == op_[1]:
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == op_[2]:
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == op_[3]:
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        if op not in op_:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
