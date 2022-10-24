#!/usr/bin/python3
"""
Contains:
    BaseGeometry class
"""


class BaseGeometry:
    """
    methods:
        area(self)
        integer_validator
    """
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input
        Args:
            name - always a string
            value: int && > than 0
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
