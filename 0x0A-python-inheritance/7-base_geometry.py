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
    	"""Validates value"""
    	if not isinstance(value, int):
    		raise TypeError("<name> must be an integer")
    	elif value <= 0:
    		raise ValueError("<name> must be greater than 0")
