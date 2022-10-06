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

    def update(self, *argv, **kwargs):
        """asigns argument with *argv"""
        lenght = len(argv)
        atrib = ['id', 'width', 'height', 'x', 'y']

        if argv is None:
            return None

        if argv:
            for elem in range(len(argv)):
                setattr(self, atrib[elem], argv[elem])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """Write the class Square that inherits from Rectangle"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))
