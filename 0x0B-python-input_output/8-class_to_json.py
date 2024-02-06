#!/usr/bin/python3
"""implementing a json function"""


def class_to_json(obj):
    """function for JSON serialization of an object:

    Args:
        obj: instance of a class
    Return:
        dictionary with simple data stru're for JSON serial'tion of an object:
    """
    return obj.__dict__
