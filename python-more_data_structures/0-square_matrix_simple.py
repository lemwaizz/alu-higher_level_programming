#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for n in matrix:
        n * n
    result = map(square_matrix_simple, matrix)
    print(result)
