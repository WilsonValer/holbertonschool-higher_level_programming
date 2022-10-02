#!/usr/bin/python3
""" my module class """


class Student():
    """ my class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method """
        dicty = self.__dict__
        if attrs:
            empty_dic = {}
            for elem in range(len(attrs)):
                if attrs[elem] in dicty:
                    empty_dic[attrs[elem]] = dicty[attrs[elem]]
            return empty_dic
        else:
            return dicty
