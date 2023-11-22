#!/usr/bin/python3
"""
Shebang for python 3
"""


class Square:
    '''creates an empty square'''
    def __init__(self, size=0, position=(0, 0)):
        """instatiate size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieves size"""
        return self.__size

    @size.setter
    def size(self, size):
        """assigns size to size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """retrieve position attribute"""
        return self.__position

    @size.setter
    def position(self, value):
        """set the value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """calculates area"""
        square_area = self.__size ** 2
        return square_area

    def my_print(self):
        """print in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for n in range(self.__size):
                for m in range(self.__position[0]):
                    print(' ', end="")
                for o in range(self.__size):
                    print("#", end="")
                print()
