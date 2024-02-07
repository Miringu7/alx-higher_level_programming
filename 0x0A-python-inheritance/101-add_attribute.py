#!/usr/bin/python3
"""defines an attribute adding method"""


def add_attribute(obj, attr_type, value):
    """function that adds a new attribute to an object if it’s possible:

    Args:
        instance: class to add attribute
        attr_type: attribute name to add
        value: attribute value added
    """
    try:
        setattr(obj, attr_type, value)
    except Exception:
        raise TypeError("can't add new attribute")
