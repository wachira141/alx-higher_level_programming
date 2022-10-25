#!/usr/bin/python3
"""
conatins:
    write_file - function
"""


def write_file(filename="", text=""):
    """
    func to write a string to a text
    Return: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return(f.write(text))
