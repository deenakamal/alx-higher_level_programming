#!/usr/bin/python3
"""Module used to define a function that prints My name"""


def say_my_name(first_name, last_name=""):
    """
    printing first and last name

    Args:
        first_name: first name
        last name: last name
    Raises:
         TypeError: if the firs name or last name not string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name))
