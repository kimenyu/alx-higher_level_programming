#!/usr/bin/python3
"""basegeometryclass"""


class BaseGeometry:
    """instance of geometry class"""
    def __init__(self):
        """initialize class"""
        pass

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(self.value, int):
            raise TypeError("<name> must be an integer")
    	elif self.value <= 0:
            raise ValueError("<name> must be greater than 0")
