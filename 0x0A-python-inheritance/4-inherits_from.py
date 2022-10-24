#!/usr/bin/python3
"""
Contains: inherits_from func
"""
def inherits_from(obj, a_class):
    """
    use issubclass to get what object is a subclass of
    Return:
    True if obj is instance of class that it inherits from or is subclass of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
