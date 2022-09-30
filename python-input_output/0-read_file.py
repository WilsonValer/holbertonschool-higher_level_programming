#!/usr/bin/python3
"""module """


def read_file(filename=""):
    """metode to read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
