#!/usr/bin/python3

""" defines a Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Implements a Rectangle class """

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
