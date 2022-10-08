#!/usr/bin/python3
"""my module class base"""
import json


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries:"""
        if not list_dictionaries or list_dictionaries is None:
            return ("[]")

        if list_dictionaries:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs"""
        filename = "{}.json".format(cls.__name__)
        my_list_dict = []

        if list_objs:
            for i in range(len(list_objs)):
                my_list_dict.append(list_objs[i].to_dictionary())
        else:
            list_objs = "[]"

        list_format_json = cls.to_json_string(my_list_dict)
        with open(filename, 'w', encoding='utf-8') as files:
            files.write(list_format_json)

    @staticmethod
    def from_json_string(json_string):
        """ returns thebb list of the JSON string representation"""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """18. Dictionary to Instance"""
        if (cls.__name__ == "Rectangle"):
            dummy = cls(4, 1)
        elif (cls.__name__ == "Square"):
            dummy = cls(9)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ that returns a list of instances:"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dictionary in obj_list:
                    result.append(cls.create(**dictionary))
                return result
        except Exception:
            return result
