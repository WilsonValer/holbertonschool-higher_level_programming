#!/usr/bin/python3
"""
This module contains matrix_divided function.
Prototype matrix_divided(matrix, div).
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    Args:
        matrix (int): list of element to divide
        div (int): divider
    Returns:
        list: the new list with all elements divided.
    """
    leng = 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_1)

    msg_2 = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(msg_1)

    if leng != 0 and len(elements) != leng:
        raise TypeError(msg_2)

    for num in elements:
        if not isinstance(num, (int, float)):
            raise TypeError(msg_1)

    leng = len(elements)

    mtx = [[round((fil[i]/div), 2) for i in range(len(fil))] for fil in matrix]
    return mtx
