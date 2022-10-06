#!/usr/bin/python3
"""my module class"""
from .base import Base


class Rectangle(Base):
    """mi class recctangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """method to calculate the area"""
        return self.__width * self.__height

    def display(self):
        """module to print charcater #"""
        for elem in range(self.__height):
            print("{}".format("#") * self.__width)

    def __str__(self):
        """representation print object"""
        str_id = str(self.id)
        str_x = str(self.__x)
        str_y = str(self.__y)
        str_width = str(self.__width)
        str_height = str(self.__height)
        result = str_x + '/' + str_y + ' - ' + str_width + '/' + str_height
        return f'[Rectangle] ({str_id})  {result}'

    @property
    def width(self):
        """return the value width"""
        return self.__width

    @property
    def height(self):
        """return height value"""
        return self.__height

    @property
    def x(self):
        """return ther value x"""
        return self.__x

    @property
    def y(self):
        """return the value y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set the new value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the nuw value height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set the new value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set the new value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
