#!/usr/bin/python3
"""importing the json module"""


import json
"""Defines an json function."""


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”:

    Args:
        filename: JSON file
    Return:
        the object created
    """
    with open(filename, encoding="utf-8") as my_obj:
        return json.load(my_obj)
