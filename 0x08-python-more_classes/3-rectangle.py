#!/usr/bin/python3
"""
define a class Rectangle with private attr width and height
public area and perimeter methods
"""
class Rectangle():
"""
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
        Area = width x height
        Perimeter = 2(width x height)
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        """
        def __init__(self, width = 0, height = 0):
            """initialize rectangle"""
            self.width = width
            self.height = height
        @property
        def width(self):
            """getter for the width attr"""
            return self.__width

        @width.setter
        def(self, value):
            """setter to set width if int and > 0"""
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

        @property
        def height(self):
            """getter for the height attr"""
            return self.__height
        @height.setter
        def height(self, value):
            """setter for the height attr"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0):
                raise ValueError('height must be >= 0')
            self.__height = value

        def area(self):
            """puvlic instance area"""
            return self.__width * self.__height
        
        def perimeter(self):
            """public instance area"""
            if self.__height or self.__with == 0:
                return 0
            return 2 * (self.__width + self.__height)

        def __str__(self):
            if self.__width or self.__height == 0:
                return ""
            rect = "\n".join(["#" * self.__width for i in range(self.__height]))
            return rect

