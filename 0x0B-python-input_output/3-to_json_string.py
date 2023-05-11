#!/usr/bin/python3
"""json"""
import json


def to_json_string(my_obj):
    """serialize"""
    obj = json.dumps(my_obj)
    return obj
