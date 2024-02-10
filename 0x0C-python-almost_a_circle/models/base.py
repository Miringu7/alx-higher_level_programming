#!/usr/bin/python3
"""first class"""


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
