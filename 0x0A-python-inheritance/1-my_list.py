#!/usr/bin/python3
"""
a class that inherits from List
"""


class MyList(list):
    """ myList class defination"""
    def print_sorted(self):
        """public instance method that prints the list"""
        print(sorted(self))
