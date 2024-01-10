#!/usr/bin/python3
'''adds all arguments to a Python list, and then save them to a file'''
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    filename = 'add_item.json'
    _object = sys.argv[1:]

    if os.path.exists(filename):
        _object = load_from_json_file(filename) + _object

    save_to_json_file(_object, filename)
