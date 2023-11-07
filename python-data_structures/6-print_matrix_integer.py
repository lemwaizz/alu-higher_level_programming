#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in range((len(matrix[0]) - 1)):
        for i in range((len(matrix)) - 1):
            print("{:d}".format(matrix[i][c]))
