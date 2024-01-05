#!/usr/bin/python3
'''The Definition of class Rectangle'''


class Rectangle:
    '''The Rectangle class'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialize a new instance'''
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Get the new Rectangle width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the new Rectangle width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''Get the new Rectangle height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the new Rectangle height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        '''get the Rectangle area'''
        return self.width * self.height

    def perimeter(self):
        '''Returns the Rectangle perimeter'''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Method for returns a string  with the character #"""
        if self.width == 0 or self.height == 0:
            return ""

        str_ = ''
        for _ in range(self.height):
            str_ += (str(self.print_symbol) * self.width) + '\n'
        return str_.strip('\n')

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''Prints a message when deleting an instance of class'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
