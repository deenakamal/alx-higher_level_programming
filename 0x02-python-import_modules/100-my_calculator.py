#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    length_ = len(sys.argv) - 1
    if length_ != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    b = sys.argv[3]

    op = sys.argv[2]
    op_ = ['+', '-', '*', '/']

    calc_ = [add, sub, mul, div]

    if op not in op_:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    for i in range(4):
        if op == po_[iterat]:
            print("{} {} {} = {}".format(a, operator, b, calc_[i](a, b)))
