#!/usr/bin/python3
"""importing the json module"""


import json
"""Defines an json function."""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:

    Args:
        my_obj: object to turn to json string
        filename: file to write the json string
    """
    with open(filename, mode='w', encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
