#!/usr/bin/python3
for c in range(ord('z'), ord('a'), -2):
    print("{}{}".format(chr(c), chr(c - 33)), end="")
