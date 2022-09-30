#!/usr/bin/python3
"""module 100-my-int"""


class MyInt(int):
    """ class my int """
    def __eq__(self, other):
        if isinstance(self, int):
            return False

    def __ne__(self, other):
        if isinstance(self, int):
            return True
