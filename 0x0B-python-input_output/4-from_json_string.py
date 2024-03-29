#!/usr/bin/python3
'''from_json_string Module'''
import json


def from_json_string(my_str):
    '''
    Returns a python object represented by a JSON string
    Args:
       my_str: string
    '''
    return json.loads(my_str)
