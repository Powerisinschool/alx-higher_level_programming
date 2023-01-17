#!/usr/bin/python3

""" Base model """

import json
import os


class Base:
    """
    This is the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function returns a json representation of a python dict
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function saves an object to a file
        """
        fp = f"{cls.__name__}.json"
        with open(fp, "w") as f:
            if list_objs is None:
                f.write("[]")
                return
            f.write(cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string in ("", "[]"):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        fp = f"{cls.__name__}.json"
        if not os.path.exists(fp):
            return []
        with open(fp, "r") as f:
            return [cls.create(**obj) for obj in cls.from_json_string(f.read())]
