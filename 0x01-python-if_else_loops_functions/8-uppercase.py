#!/usr/bin/python3
def uppercase(str):
    for char_ in str:
        if ord(char_) >= 97 and ord(char_) <= 122:
            char_ = chr(ord(char_) - 32)
            print("{:s}".format(char_), end="")
    print("")
