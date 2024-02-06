#!/usr/bin/python3
"""importing the json module"""


import json
"""Defines an json function."""


def to_json_string(my_obj):
    """ function that  returns the JSON representation of an object (string):

    Args:
        my_obj: object to turn to string
    Return:
         JSON representation of an object (string):
    """
    return json.dumps(my_obj)
