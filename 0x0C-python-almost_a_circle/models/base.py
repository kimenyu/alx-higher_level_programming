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
        """return json"""
        return json.dumps(list_dictionaries or [])
    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + '.json'
        my_list = []
        if list_objs:
            my_list = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, mode = 'w') as f:
            f.write(cls.to_json_string(my_list))
            #json.dump(my_list, f)
    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            datan = json.loads(json_string)
            return datan
