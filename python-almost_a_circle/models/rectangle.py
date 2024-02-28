#!/usr/bin/python3
"""
This is a rectangle that inherits from base
"""

from models.base import Base


class Rectangle(Base):
    """This is the rectangle class with various private attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a class constructor"""

        super().__init__(id)
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

        if type(value) != int:
            raise TypeError("Height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be greater than 0.")
        self.__height = value

    @property
    def x(self):
        """property getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setting for x"""

        if type(value) != int:
            raise TypeError("x must be an integer.")
        if x < 0:
            raise ValueError("x must be >= 0.")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""

        if type(value) != int:
            raise TypeError("y must be an integer.")
        if y < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value
