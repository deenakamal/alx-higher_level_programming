#!/usr/bin/python3
"""square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
            f"- {self.height}"

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size getter method"""
        self.width = value
        self.height = self.width

    def update(self, *args, **kwargs):
        """update info for instance of Square class"""
        if args:
            attr_list = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise ValueError(f"{key} is not attribute in this class")

    def to_dictionary(self):
        """to dictionary"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
