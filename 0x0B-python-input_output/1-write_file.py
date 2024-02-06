#!/usr/bin/python3
"""Defines a writing function."""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8):

    Args:
        filename [file]: file to be read
        text: string to write
    Return:
         number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as my_file:
        my_file.write(text)
    with open(filename, encoding="utf-8") as my_file:
        num_char = 0
        while True:
            line = my_file.readline()
            if not line:
                break
            for char in line:
                num_char += 1
    return num_char
