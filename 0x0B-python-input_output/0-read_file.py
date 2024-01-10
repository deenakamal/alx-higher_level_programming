#!/usr/bin/python3
'''read_file function'''


def read_file(filename=""):
    '''
    Reads a text file && prints it to stdout

    Args:
        filename: file name
    '''

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
