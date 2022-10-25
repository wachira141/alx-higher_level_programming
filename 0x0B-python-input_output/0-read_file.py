#!/usr/bin/python3
"""
Contains:
    read_file(filenanem) func
"""


def read_file(filename=""):
    """
    func to read a text file(utf8)
    print to stdout
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end='')
