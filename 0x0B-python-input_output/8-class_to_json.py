#!/usr/bin/python3
'''class_to_json function Module'''


def class_to_json(obj):
    '''Returns the dictionary description
    with simple data structure'''
    return obj.__dict__
