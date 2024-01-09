#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr_, value):
    """Add a new attribute to an object if possible.
    Args:
        obj: The object
        attr_: The name of the attribute
        value: The value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_, value)
