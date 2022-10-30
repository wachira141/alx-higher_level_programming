#!/usr/bin/python3
"""
Contains the Base class
"""
import json

class Base:
    """
        private class attr __nb_object
        instance attr id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return JSON string of list_dictionary
            if list_dictionary is empty or None:
                Return []
            else JSON string representation
            """
            if list_dictionaries is None or len(list_dictionaries) == 0:
                return '[]'
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to write JSON string to a file
        Args:
            cls - class
            list_objs - list of instance who inherits of Base
        """
        filename = cls.__name__ + '.json'

        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_string):
        """Return the deserealized of a JSON string"""
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method to return an instance"""
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        """return a list of instance"""
        fileN = cls.__name__ + '.json'
        newlist = []
        try:
            
            with open(fileN, 'r') as f:
                inst = cls.from_json_string(f.read())
            for i, dict in enumerate(instances):
                newlist.append(cls.create(**inst[i]))
        except Exception:
            pass
        return newlist
