#!/usr/bin/python3
"""saves to json file"""
import json


def save_to_json_file(my_obj, filename):
    """saves to json file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dump(my_obj)
