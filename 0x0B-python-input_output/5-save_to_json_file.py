#!/usr/bin/python3
"""
Contains a func to write an Obj to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to write the text file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
