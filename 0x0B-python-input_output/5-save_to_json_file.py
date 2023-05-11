#!/usr/bin/python3
"""saves to json file"""
import json


def save_to_json_file(my_obj, filename):
    """saves to json file"""
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
