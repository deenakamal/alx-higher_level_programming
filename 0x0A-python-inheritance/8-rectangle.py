#!/usr/bin/python3
"""Module Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ define subclass Rectangle."""
    def __init__(self, width, height):
        '''Define Constructor '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height