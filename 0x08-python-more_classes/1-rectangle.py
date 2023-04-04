#!/usr/bin/python3
"""
A module class that defines rectangle
"""


class Rectangle:
    """ Creating a private instance"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """Property to retreive it"""
    @property
    def width(self):
    	return self.__width
    

    """creating a property setter for width"""
    @width.setter
    def width(self, value):
        if(type(value) is not int):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
            self.__width = value

    """Creating a property to retrieve it"""

    @property
    def height(self):
    	return self.__height

    """Creating  a property setter for height"""

    @height.setter
    def height(self, value):
        if(type(value) is not int):
            raise TypeError("height must be an integer")
        elif(value < 0):
            raise ValueError("height must be >= 0")
            self.__height = value
