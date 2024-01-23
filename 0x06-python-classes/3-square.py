#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initialization of a new square
        Args:
            size: the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Represents a method"""
    def area(self):
        """area method taking the self.size
        Return:
            square value of the size variable
        """
        return (self.__size ** 2)
