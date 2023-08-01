#!/usr/bin/python3
"""writes an objects to a json rep"""
import json


def save_to_json_file(my_obj, filename):
    """with open"""
    with open(filename, 'w') as f:
	return json.dump(my_obj, f)

