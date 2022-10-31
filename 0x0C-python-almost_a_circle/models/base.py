#!/usr/bin/python3
"""
Contains the Base class
"""
import json
import csv
import turte


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """cls method to serialize into a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """cls method to deserealize from a csv file"""
        filename = cls.__name__

        with open(filename, 'r', 'newline') as csvfile:
            if cls.__name__ == 'Rectangle':
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
            list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
