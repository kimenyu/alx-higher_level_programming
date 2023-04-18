#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """instantiate a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        if not isinstance(position, tuple) or len(position) != 2 or not isinstance(position[0], int) or not isinstance(position[1], int) or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
