#!/usr/bin/python3

""" defines a square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implements a square class using rectangle"""

    def __init__(self, size):
        """ constructor

        Args:
            size (int): private size
        """
        super().__init__(size, size)
