#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda m: list(map(lambda f: f*f, m)), matrix))
