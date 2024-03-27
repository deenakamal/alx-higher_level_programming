#!/usr/bin/python3
"""Find a Peak"""


def find_peak(list_of_integers):
    """Functon that Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    return (max(list_of_integers))
