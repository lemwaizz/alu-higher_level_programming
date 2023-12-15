#!/usr/bin/python3
"""function that divides a matrix with a number"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix """
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")
        if len(i) != matrix[0]:
            raise TypeError("Each row of the matrix must have the same size")
            for item in i:
                if item not isinstance(item, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists)"
                                    "of integers/floats")
    if div not isinstance(div, int) or not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list())
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j]/div, 2))
    return new_matrix
