#!/usr/bin/python3
"""
Shebang for python 3
"""


class Square:
    '''creates an empty square'''
    def __init__(self, size=0):
        """instatiate size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area"""
        square_area = self.__size ** 2
        return square_area
