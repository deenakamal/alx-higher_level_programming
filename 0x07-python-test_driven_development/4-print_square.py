#!/usr/bin/python3
""" Module to define a function that prints a square"""


def print_square(size):
    """
    print square

    Args:
        size: the length of the square

    Raises:
         TypeError: if size not integer or
                if size is a float and is less than 0
         ValueError: if size is less than 0

    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print('#' * size)
