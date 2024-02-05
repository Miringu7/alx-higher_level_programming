#!/usr/bin/python3

""" defines a square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ constructor

        Args:
            size (int): private size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
