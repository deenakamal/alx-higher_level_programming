#!/usr/bin/python3
""" MyList Module """


class MyList(list):
    """ Define MyList Class """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        print(sorted(self))
