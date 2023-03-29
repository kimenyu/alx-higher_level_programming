#!/usr/bin/python3
"""Working on op with python"""


class Square():
    """Class representing a square"""

    def __init__(self, size=0):
        """ initialize the class with a private square attribute"""

        try:
            if (typeof(size) is not int):
                raise TypeError("size must be an integer")
            else if(size < 0):
                raise ValueError("size must be >= 0")
        self.__size = size
