#!/usr/bin/python3
"""Create an empty class"""


class Square:
    """Instantiate size as private attribute """
    def __init__(self, size=0):
        self.__size = size


    """propert"""
    @property
    def size(self):
        """getter method"""
        return self.__size

    """setter"""
    @size.setter
    def size(self, value):
        """instantiate"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
