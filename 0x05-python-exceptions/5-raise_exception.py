#!/usr/bin/python3

def raise_exception():
    """function that raises a type exception."""
    try:
        raise TypeError
    except TypeError:
        raise
