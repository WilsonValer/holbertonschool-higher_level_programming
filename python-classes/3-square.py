#!/usr/bin/python3
"""class Square"""


class Square:

    """defines a Private instance attribute"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError("size must be an integer")

    def area(self):
        ar = self.__size ** 2
        return ar
