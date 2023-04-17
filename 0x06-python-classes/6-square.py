#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """instantiate a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

            self.__position = value

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
