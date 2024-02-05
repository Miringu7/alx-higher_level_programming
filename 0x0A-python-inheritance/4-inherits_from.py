#!/usr/bin/python3

""" defines a function """


def inherits_from(obj, a_class):
    """ function that checks object alongside class

    Args:
        obj: object to be checked
        a_class: specified class

    Returns:
        True if the object is exactly an instance
        of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    """

    if (isinstance(obj, a_class)) and not (type(obj) == a_class):
        return True
    return False

