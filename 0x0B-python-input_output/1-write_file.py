#!/usr/bin/python3
'''write_file function'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file

    Args:
        filename: file name
        text: text to a file
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
