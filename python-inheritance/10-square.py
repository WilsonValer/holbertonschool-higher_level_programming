#!/usr/bin/python3
"""Class rectangle inherent"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ clas Square """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
