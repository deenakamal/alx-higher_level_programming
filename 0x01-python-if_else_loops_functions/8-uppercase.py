#!/usr/bin/python3
def uppercase(str):
    for char_ in str:
        if ord(char_) >= 97 and ord(char_) <= 122:
            print("{:c}".format(65 + (ord(char_) - 97)))
        else:
            print(char_ end="")
    print("")
