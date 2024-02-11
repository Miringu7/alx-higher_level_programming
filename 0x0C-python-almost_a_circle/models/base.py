#!/usr/bin/python3
"""first class"""
import json
"""imports json"""


class Base():
    """declare the base class

    Args:
        __nb_objects: private attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
            id: identifier
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """adding the static method
        Args:
            list_dictionaries: list of dictionaries
        return:
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            try:
                return json.dumps(list_dictionaries)
            except TypeError as e:
                return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """class method
        Args:
            list_objs: list of instances who inherits of Base
        """
        if list_objs is None:
            with open("Rectangle.json", mode='w', encoding="utf-8") as my_json:
                my_json.write('[]')
        with open("Rectangle.json", mode='w', encoding="utf-8") as my_json:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            my_json.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """adding the static method
        Args:
            json_string: string representing a list of dictionaries
        return:
             empty list Otherwise, the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
