#!/usr/bin/python3
"""
Contains:
    func to append a string at endd
"""


def append_write(filename="", text=""):
    """
    Note:
    this function appends a string
    Return:
        return the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return(f.write(text))
