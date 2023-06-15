#!/usr/bin/python3
"""Creating a class square"""


class Square:
    """square"""
    def __init__(self, size=0):
        """"instatiation"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
