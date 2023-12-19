#!/usr/bin/python3
"""square class"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """init
        Args:
            size: size
        """
        self.size = size

    @property
    def size(self):
        """get the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """print a square of #"""
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
