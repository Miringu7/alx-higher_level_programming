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

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #
        """
        if self.__y > 0:
            for i in range(self.__y):
                print("")
        for h in range(self.__height):
            if self.__x > 0:
                for j in range(self.__x):
                    print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns string [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
              self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        Args:
            args: stdin method arguments
            kwargs: function dictionary arguments
        """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if len(kwargs) >= 1:
                for key, value in kwargs.items():
                    if key == "x":
                        self.__x = value
                    if key == "y":
                        self.__y = value
                    if key == "height":
                        self.__height = value
                    if key == "width":
                        self.__width = value
                    if key == "id":
                        self.id = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return {
                'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.__height,
                'width': self.__width
               }
