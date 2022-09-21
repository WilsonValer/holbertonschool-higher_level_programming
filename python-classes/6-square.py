#!/usr/bin/python3
"""class Square"""


class Square:

    """defines a Private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        ar = self.__size ** 2
        return ar

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[0] >= 0:
                    print(" " * self.__position[0], end='')
                print("#" * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
