#!/usr/bin/python3

""" defines a MyInt class """


class MyInt(int):
    """overides the equality and in equality methods"""
    def __eq__(self, other):
        """ inverts the == operator

        Args:
            other: value
        Return:
            inverted ==
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ inverts the != operator

        Args:
            other: value
        Return:
            inverted !=
        """
        return super().__eq__(other)
