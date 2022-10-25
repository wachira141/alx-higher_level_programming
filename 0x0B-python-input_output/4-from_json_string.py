#!/usr/bin/python3
"""
Contains a func that returns a py ds
"""
import json


def from_json_string(my_str):
    """
    Return - a python data structure
    """
    return json.loads(my_str)
