#!/usr/bin/python3
"""
This module contains add_integer function.
Prototype def add_integer(a, b=98)
Function that adds two integer numbers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    @:a (int): first integer
    @:b (int): second integer
    Returns:int: the sum of a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
