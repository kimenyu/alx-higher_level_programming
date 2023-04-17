#!/usr/bin/python3
""" rectangle class"""
from models.base import Base



class Rectangle(Base):
    """initiate"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """super"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        
    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """sets x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y"""
        self.__y = value
