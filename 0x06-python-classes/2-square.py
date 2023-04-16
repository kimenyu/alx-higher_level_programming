#!/usr/bin/python3
"""Create an empty class"""


class Square:
    """Instantiate size as private attribute """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """instantiate"""
        if(type(size) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value
