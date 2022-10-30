#!/usr/bin/python3
"""
    Contains class square that inherits from Rectangle
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square
            inherits all the attr from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init a new class square
        Args:
            size(int): The size of the square
            x(int): ThE X Cord of the square
            y(int): The y cord of the square
            id(int): the identity of the square
        """
        super().__init(size, size, x, y, id)

        @property
        def size(self):
            """Size getter"""
            return self.width

        @size.setter
        def size(self, value):
            """size setter"""
            self.width = value
            self.height = value

        def update(self, *args, **kwargs):
            """public method update with args and kwargs method"""
            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        self.id = arg
                    elif a == 1:
                        self.size = arg
                    elif a == 2:
                        self.x = arg
                    else:
                        self.y = arg
                a += 1

            else:
                for k, v in kwargs.items():
                    if k == 'id':
                        self.id = value
                    elif k == 'size':
                        self.size == value
                    elif k == 'x':
                        self.x = value
                    else:
                        self.y = value

        def to_dictionary(self):
            """method to return dict representation"""
            return {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                    }

