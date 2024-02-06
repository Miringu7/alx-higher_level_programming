#!/usr/bin/python3

""" defines a square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ implements a square class using Rectangle"""

    def __init__(self, size):
        """ constructor

        Args:
            size (int): private size
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str()representation of a square"""
        my_str = "[" + str(Rectangle.__name__) + "] "
        my_str += str(self.__size) + "/" + str(self.__size)
        return my_str
