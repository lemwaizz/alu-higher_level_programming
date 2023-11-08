#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for n in matrix:
        new_matrix = map(lambda n: n * n, matrix)
        return new_matrix
