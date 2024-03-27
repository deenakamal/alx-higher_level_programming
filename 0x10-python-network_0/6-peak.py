#!/usr/bin/python3
"""Find a Peak"""


def binary_search(list_of_integers, start, end):
    """ performs the recursive binary search """
    if not list_of_integers:
        return None
    if start == end:
            return list_of_integers[start]

    mid = (start + end) // 2
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return binary_search(list_of_integers, mid + 1, end)
    else:
        return binary_search(list_of_integers, start, mid)

def find_peak(list_of_integers):
    """Functon that Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
