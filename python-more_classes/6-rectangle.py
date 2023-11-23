#!/usr/bin/python3
"""create empty class for a rectangle"""


class Rectangle:
    """Instantiate empty class"""
    def __init__(self, width=0, height=0):
        number_of_instances = 0
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """assign width to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assigns height to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area"""
        rec_area = self.__height * self.__width
        return rec_area

    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            rec_perimeter = 0
        else:
            rec_perimeter = (self.__width + self.__height)*2
        return rec_perimeter

    def __del__(self):
        """detects when an instance of rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """prints int stdout"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rect = rect + "#"
                rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """return string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
