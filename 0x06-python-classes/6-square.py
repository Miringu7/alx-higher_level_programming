#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of a new square
        Args:
            size: the size of the new square
            position: the position of new square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Property to retrieve the private instance attribute
        Return:
            self.__position: the gotten private instance attribute
        """
        return self.__position

    """Represents a method"""
    @position.setter
    def position(self, value):
        """property setter to set the position attribute"""
        if (not isinstance(value, int) or
           len(value) != 2 or
           not all(isinstance(num, int) for num in value) or
           not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for y in range(0, self.__position[0]):
                    print(' ', end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
