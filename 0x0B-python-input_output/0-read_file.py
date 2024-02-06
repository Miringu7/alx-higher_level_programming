#!/usr/bin/python3
"""Defines a reading function."""


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout:

    Args:
        filename [file]: file to be read
    """
    with open(filename, encoding="utf-8") as my_utf:
        print(my_utf.read(), end="")
