#!/usr/bin/python3

""" defines an geometry class """


class BaseGeometry():
    """ Implements an area function on geometry class """

    def area(self):
        """ area function

        Raises:
            Exception: area() is not implemented
        """
        raise Exception ("area() is not implemented")

    def integer_validator(self, name, value):
        """ valdiates value

        Args:
            name: the name
            value: the value

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError (name + " must be an integer")
        if value <= 0:
            raise ValueError (name + " must be greater than 0")
