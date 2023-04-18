#!/usr/bin/python3
""" rectangle class"""
from models.base import Base



class Rectangle(Base):
    """initiate"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """super"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validator(self,name, value):
        """validates"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == 'width' or name == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

        
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
        self.validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        self.validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """sets x"""
        self.validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y"""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """returns area"""
        return self.width * self.height

    def display(self):
        """display a rectable of '#' """
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
   
    def __str__(self):
        """string representative of class"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'
