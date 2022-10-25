#!/usr/bin/python3
"""
Contains - func that creates an obj from json
"""
import json


def load_from_json_file(filename):
    """
    Func to create an obj
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
