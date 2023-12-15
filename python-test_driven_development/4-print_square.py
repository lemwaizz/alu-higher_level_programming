#!/usr/bin/python3
"""Function that prints square"""


def print_square(size):
    """A function that prints a square as #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    
