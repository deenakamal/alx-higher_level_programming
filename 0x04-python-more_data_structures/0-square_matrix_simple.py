#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        sub_matrix = []
        for num in row:
            sub_matrix.append(num ** 2)
        new_matrix.append(sub_matrix)
    return new_matrix
