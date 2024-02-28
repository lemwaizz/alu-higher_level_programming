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
