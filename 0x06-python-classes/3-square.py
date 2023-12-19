#!/usr/bin/python3
"""square class"""


class Square:
    """define square class """

    def __init__(self, size=0):
        """
        init

        Args:
            size: size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """get the area of a square"""
        return self.__size * self.__size
