#!/usr/bin/python3
"""
contains method lookups and return obj attr and methods
"""


def lookup(obj):
    """
    function that returns the list of available attr and methods of an obj
    """
    return dir(obj)
