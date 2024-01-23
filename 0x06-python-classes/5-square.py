#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initialization of a new square
        Args:
            size: the size of the new square
        """
        self.__size = size

    """Represents a method"""
    @property
    def size(self):
        """Property to retrieve the private instance attribute
        Return:
            self.__size: the gotten private instance attribute
        """
        return self.__size

    """Represents a method"""
    @size.setter
    def size(self, value):
        """property setter to set the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Represents a method"""
    def area(self):
        """area method taking the self.size
        Return:
            square value of the size variable
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints out the square in #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()
