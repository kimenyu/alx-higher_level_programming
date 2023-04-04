#!/usr/bin/python3
"""class Rectangle  to define a rectangle"""
class Rectangle:
    """ Creating a private instance"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve it"""
        return self._width

    @width.setter
    def width(self, value):
        """creating a property setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Creating a property to retrieve it"""
        return self._height

    @height.setter
    def height(self, value):
        """Creating  a property setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
