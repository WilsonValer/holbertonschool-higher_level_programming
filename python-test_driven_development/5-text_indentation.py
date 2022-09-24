#!/usr/bin/python3
"""
This module contains print_square function.
Prototype def print_square(size)
Function that prints a square.
"""


def text_indentation(text):
    """
    function that prints a square with the character #.
    Args: size: size of square to print
    Returns: Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cut = ".?:"
    length = len(text)
    flag = False
    for j in range(length):
        if flag:
            if text[j] == " ":
                continue
            flag = False
        if text[j] == cut[0] or text[j] == cut[1] or text[j] == cut[2]:
            print("{}\n".format(text[j]))
            flag = True
        else:
            print(text[j], end='')
