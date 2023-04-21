#!/usr/bin/python3
"""Creating a class"""
import json


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inits the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json"""
        if list_dictionaries ==  None:
            return ""
        else:
            data = json.dumps(list_dictionaries)
            return data
