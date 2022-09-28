#!/usr/bin/python3
""" print_sorted """


class MyList(list):
    """class list that sorted """
    def print_sorted(self):
        """ method to sorted a list """
        print(sorted(self))
