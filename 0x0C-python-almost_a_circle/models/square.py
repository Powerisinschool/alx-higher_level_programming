#!/usr/bin/python3

""" Square model """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the square class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__
        Return the string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        This function updates the properties of the rectangle
        """
        attributes = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, attributes[i], args[i])
            if i == len(args) - 1:
                return

        for name, value in kwargs.items():
            setattr(self, name, value)
