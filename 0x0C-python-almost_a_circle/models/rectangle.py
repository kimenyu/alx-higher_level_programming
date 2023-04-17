#!/usr/bin/python3
"""Creating a class"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inits the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Rectangle(Base):
    """initializes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        

    def get_width(self):
        return self._width

    def set_width(self, value):
        self._width = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        self._height = value

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value
