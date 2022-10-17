#!/usr/bin/python3
""" Class Rectangle that defines rectabgle """
class Rectangle():
    """
    class rectangle defined
    """
    def __init__(self, width = 0, height = 0):
        """ class instance method """
        self.width = width
        self.height = height
    @property
    def width(self):
        """getter propert"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter property"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter propert for height"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter propert for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
