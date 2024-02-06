#!/usr/bin/python3
"""importing the json module"""


import json
"""Defines an json function."""


def from_json_string(my_str):
    """ function that  returns an object represented by a json string:

    Args:
        my_str: json string
    Return:
         returns an object (Python data structure) :
    """
    with open("my_str.txt", mode='w', encoding="utf-8") as my_file:
        my_file.write(my_str)
    with open("my_str.txt", encoding="utf-8") as my_file:
        return json.load(my_file)
