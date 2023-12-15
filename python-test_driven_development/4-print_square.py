#!/usr/bin/python3
"""Function that prints square"""


def print_square(size):
    """A function that prints a square as #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    character = "#"
    for i in range(size):
        print(character, end='')
