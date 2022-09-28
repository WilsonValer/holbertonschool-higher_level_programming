#!/usr/bin/python3
"""class"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of
    a class that inherited (directly or indirectly) """
    return isinstance(obj, a_class)
