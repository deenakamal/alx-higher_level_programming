#!/usr/bin/python3
"""
Defines add_integer module that adds two integers

"""


def add_integer(a, b=98):
    """ Add two integers

    Args:
        a (int): first integer
        b (int): second integer

    Return: sum of a and b,
              otherwise raise a TypeError if not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
