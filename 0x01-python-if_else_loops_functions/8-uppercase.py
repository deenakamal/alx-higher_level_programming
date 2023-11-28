#!/usr/bin/python3
def uppercase(str):
    for char_ in str:
        if ord(char_) >= ord('a') and ord(char_) <= ord('z'):
            char_ = chr(ord(char_) - 32)
            print("{}".format(char_), end="")
    print("")
