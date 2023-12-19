#!/usr/bin/python3
""" class square """


class Square:
    """ implementation of square class """

    def __init__(self, size=0):
        """Initializes the square instance.

        Args:
            size: size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
