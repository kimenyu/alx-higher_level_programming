#!/usr/bin/python3
"""
Module 2-rectangle
Contains class Rectangle
with private attribute width and height
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def area(self):
        """instance to calculate the area"""
        return self.__width * self.__height

    @property
    def perimeter(self):
        """public instance method to calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            return 2 *(self.__width + self.__height)

