#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance of"""


def is_same_class(obj, a_class):
    """
    use type() to get specific class
    use isinstance to get if obj is of specified type

    Return:
        true if obj is exactly an instance
    """
    return type(obj) == a_class
