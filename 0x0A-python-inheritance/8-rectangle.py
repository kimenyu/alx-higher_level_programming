#!/usr/bin/python3
"""create an empty class"""


class BaseGeometry:
    """empty class """
    pass

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Integer validator"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
"""class inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """inherits"""
    def __init__(self, width, height):
        """instantiates class object"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
