#!/usr/bin/python3
"""Defines an appending function."""


def append_write(filename="", text=""):
    """ function that appends a string to a text file (UTF8):

    Args:
        filename [file]: file to be read
        text: string to append
    Return:
         number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)
