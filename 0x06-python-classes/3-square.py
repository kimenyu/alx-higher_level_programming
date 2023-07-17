#!/usr/bin/python3
"""an empty class that defines a square
"""


class Square:
    """class square with private instance atrribute size
    """
    def __init__(self, size=0):
        """class atrribute

        Args:
            size (int): a private intance atrribute
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        
    def area(self):
        """public instance method area that returns the urrent square area
        """
        return self.__size * self.__size
