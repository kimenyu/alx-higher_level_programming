#!/usr/bin/python3
"""Creating a class"""


class Base:
    """init"""

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
"""creating a subclass"""


class Rectangle(Base):
    """initiate"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        

    def get_width(self):
        return self.__width

    def set_width(self, value):
        self.__width = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        self.__height = value

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value
