#!/usr/bin/python3
"""function for pascal's triangle
"""


def pascal_triangle(n):
    """function itself"""
    n = 5
    list = []
    for i in range(n+1):
        for j in range(0, n-i):
            C = 1
            for j in range(1, i+1):
                C = C * (i - j) // j
        list.append(C)
        return list
    if n < 0:
        return []
