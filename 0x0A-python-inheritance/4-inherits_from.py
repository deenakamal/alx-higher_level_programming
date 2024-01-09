#!/usr/bin/python3
"""inherits_from Module """


def inherits_from(obj, a_class):
    """returns True if the object is an instance
     otherwise returns False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
