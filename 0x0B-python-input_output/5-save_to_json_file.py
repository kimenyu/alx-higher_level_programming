#!/usr/bin/python3
"""saves to json file"""
import json


def save_to_json_file(my_obj, filename):
    """saves to json file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            json.dump(my_obj, f) 
