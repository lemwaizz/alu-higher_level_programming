#!/usr/bin/python3
"""create empty class for a rectangle"""


class Rectangle:
    """Instantiate empty class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)

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
                    rect = rect + str(self.print_symbol)
                rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """return string representation of rectangle"""
        return "Rectangle({}, {})".format(self.print_symbol, self.print_symbol)
