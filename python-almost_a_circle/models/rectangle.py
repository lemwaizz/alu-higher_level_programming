#!/usr/bin/python3
"""
This is a rectangle that inherits from base
"""

from models.base import base


class Rectangle(Base):
    """This is the rectangle class with various private attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a class constructor"""

        super.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """assign width to width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setting width to trust it then push it"""

        if type(value) != int:
            raise TypeError("Width must be an integer.")
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """getting the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setting conditions for value"""

        if value not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be greater than 0.")
        self.__height = value
