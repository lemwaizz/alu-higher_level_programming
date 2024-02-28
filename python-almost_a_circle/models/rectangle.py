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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """assign width to width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setting width to trust it then push it"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setting conditions for value"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setting for x"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """validate setter methods"""

        if len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

        elif len(kwargs) != 0:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.__width = kwargs["width"] if "width" in kwargs \
                else self.__width
            self.__height = kwargs["height"] if "height" in kwargs \
                else self.__height
            self.__x = kwargs["x"] if "x" in kwargs else self.__x
            self.__y = kwargs["y"] if "y" in kwargs else self.__y
