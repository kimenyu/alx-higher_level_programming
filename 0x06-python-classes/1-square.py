#!/usr/bin/python3

"""
Defining a class based on 0-square.py
"""

class Square:
    """
    Class square definition

    Args:
        size: size of a square
    """
    def __init__(self, size):
        """
        instatiates square

        Attribute:
            size: size of a side of a square
        """
        self.__size = size
