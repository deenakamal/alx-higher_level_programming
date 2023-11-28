#!/usr/bin/python3
for i_ in range(100):
    if i_ < 99:
        print("{:02d}, ".format(i_), end="")
    else:
        print("{:02d}".format(i_))
