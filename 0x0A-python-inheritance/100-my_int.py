#!/usr/bin/python3
""" Define the class MyInt """


class MyInt(int):
    """Implement"""

    def __eq__(self, other):
        """ != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """ == is now !="""
        return int(self) == other
