#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""
class Rectangle():
    """
    Define a rectangle class
    Private args
     width
     height
    public instance
        def(area)
        def perimeter()
    """
    def __init__(self, width = 0, height = 0):
        """instance method"""
        self.height = height
        self.width = width
    @property
    def width(self):
        """width getter"""
        return self.__width
    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__weight = value
    @propert
    def height(self):
        """height getter"""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height
    def perimeter(self):
        """return the primeter of the rectangle"""
        if self.__width or self.__height == 0:
            return 0
        reuturn 2 * (self.__height + self.__width)

