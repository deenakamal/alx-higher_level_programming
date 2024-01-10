#!/usr/bin/python3
'''save_to_json_file function'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an Object to a text file
    using a JSON representation

    Args:
       my_obj: python object to file
       filename: file name
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
