#!/usr/bin/python3
""" BaseGeometry Module """


class BaseGeometry:
    """Define BaseGeometry """
    def area(self):
        """ used to calculate the area."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """used to  validate the input value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
