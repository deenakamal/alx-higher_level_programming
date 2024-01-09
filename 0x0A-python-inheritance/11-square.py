#!/usr/bin/python3
'''Module Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''subclass of rectangle.'''
    def __init__(self, size):
        '''Define Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''get the area of square.'''
        return self.__size ** 2

    def __str__(self):
        '''print string representation of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
