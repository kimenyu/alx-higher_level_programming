#!/usr/bin/python3
"""creates an object from a json file"""
import json


def load_from_json_file(filename):
    """retuns"""
    with open(filename) as f:
	return json.load(f)
