#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle
"""importing the Rectangle class"""


class Square(Rectangle):
    """declare the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        Args:
            size: square size
            x: 2nd parameter
            y: 3rd parameter
            id: identifier
	"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overides str
        Return:
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
              self.x, self.y, self.height)

    @property
    def size(self):
        """returns width value"""
        return self.width

    @size.setter
    def size(self, width):
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

        self.width = width
        self.height = width
