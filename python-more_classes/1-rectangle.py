#!/usr/bin/python3
"""
Empty class that defines a Rectangle
"""


class Rectangle():
    """Empty class Rectangle"""
    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("width must be an integer")

        if width < 0 or height < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height



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
    def width():
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")


        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


