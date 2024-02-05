#!/usr/bin/python3

""" defines a rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a rectangle class using BaseGeometry """

    def __init__(self, width, height):
        """ constructor

        Args:
            width (int): private width
            height (int): private height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        my_str = "[" + str(self.__class__.__name__) + "] "
        my_str += str(self.__width) + "/" + str(self.__height)
        return my_str
