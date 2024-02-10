#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base
"""importing the base class"""


class Rectangle(Base):
    """declare the rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
        Args:
            width: rectangle width
            height: rectangle height
            x: third parameter
            y: forth parameter
        Raises:
            TypeError: if width, height, x, y not int
            ValueError: if width, height, x, y less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not width >= 0:
            raise ValueError("width must be > 0") 
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not height >= 0:
            raise ValueError("height must be > 0") 

        super().__init__(id)
        self.__width = width
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if not x >= 0:
            raise ValueError("x must be >= 0")
        if not y >= 0:
            raise ValueError("y must be >= 0")

        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of rectangle
        Args:
            width: parameter
       Raises:
            TypeError: if width not int
            ValueError: if width less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not width >= 0:
            raise ValueError("width must be > 0") 
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """sets height
        Args:
            height: parameter
       Raises:
            TypeError: if height not int
            ValueError: if height less than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not height >= 0:
            raise ValueError("height must be > 0") 
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """sets x
        Args:
            x: parameter
       Raises:
            TypeError: if x not int
            ValueError: if x less than 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not x >= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """sets y
        Args:
            y: parameter
       Raises:
            TypeError: if y not int
            ValueError: if y less than 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if not y >= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """area of rectangle function
        Returns:
            the area value	
        """
        return self.__width * self.__height
