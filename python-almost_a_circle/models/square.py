#!/usr/bin/python3
"""my module square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ my class square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property for getter"""
        return self.width

    @size.setter
    def size(self, value):
        """property for setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Write the class Square that inherits from Rectangle"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))
