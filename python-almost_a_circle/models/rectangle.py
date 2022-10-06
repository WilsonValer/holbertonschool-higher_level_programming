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
        """ change str representantion when print object """
        id_str = str(self.id)
        w_str = str(self.__width)
        h_str = str(self.__height)
        x_str = str(self.__x)
        y_str = str(self.__y)
        div_str = x_str + '/' + y_str + ' - ' + w_str + '/' + h_str
        return ("[Rectangle] " + '(' + id_str + ') ' + div_str)

    def display(self):
        """ prints the rectangle using # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *argv):
        """asigns argument with *argv"""
        lenght = len(argv)
        atrib = ['id', 'width', 'height', 'x', 'y']

        if argv is None:
            return None

        if argv:
            for elem in range(len(argv)):
                setattr(self, atrib[elem], argv[elem])

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
