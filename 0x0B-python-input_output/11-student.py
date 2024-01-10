#!/usr/bin/python3
'''Student class'''


class Student:
    '''Student class'''
    def __init__(self, first_name, last_name, age):
        '''Initialize a new instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary'''
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__

        _dict = {}
        for key in attrs:
            if hasattr(self, key):
                _dict[key] = getattr(self, key)
        return _dict

    def reload_from_json(self, json):
        '''Replaces all attribute'''
        for key, value in json.items():
            setattr(self, key, value)
