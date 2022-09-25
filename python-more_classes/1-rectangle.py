#!/usr/bin/python3
"""
Empty class that defines a Rectangle
"""


class Rectangle():
    """Empty class Rectangle"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("width must be an integer")

        if width < 0 or height < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

    def __str__(self):
        print("{} - {}".format(my_rectangle.width, my_rectangle.height))

    @property
    def height(self):
        self.__height = height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")


        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


