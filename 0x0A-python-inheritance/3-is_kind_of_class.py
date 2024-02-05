#!/usr/bin/python3

""" defines a function """


def is_kind_of_class(obj, a_class):
    """ function that checks object alongside class

    Args:
        obj: object to be checked
        a_class: specified class

    Returns:
        True if the object is exactly an instance
        of the specified class ; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    return False
