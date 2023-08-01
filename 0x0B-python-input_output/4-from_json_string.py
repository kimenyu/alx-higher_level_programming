#!/usr/bin/python3
"""returns an obj from json"""
import json


def from_json_string(my_str):
    """loads from json str"""
    return json.loads(my_str)
