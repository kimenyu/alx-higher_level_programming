#!/usr/bin/python3
"""
This module contains a Rectangle class
"""


class Rectangle:
     """ This class defines a Rectangle. It takes 2 attributes
    width and height which are both integers
    """
    def __init__(self, width=0, height=0):
        """ initializes a Rectangle instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    
    @property
    def width(self):
        """ This should get the width"""
    	return self.__width
    

    
    @width.setter
    def width(self, value):
        """ This assigns value to width"""
        if(type(value) is not int):
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
            self.__width = value


    @property
    def height(self):
        """ This retrieves the private attribute height"""
    	return self.__height

    

    @height.setter
    def height(self, value):
        """ This asigns a new value to attribute height"""
        if(type(value) is not int):
            raise TypeError("height must be an integer")
        elif(value < 0):
            raise ValueError("height must be >= 0")
            self.__height = value
