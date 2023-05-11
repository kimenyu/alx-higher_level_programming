#!/usr/bin/python3
"""to pytjon"""
import json


def load_from_json_file(filename):
    """loads"""
    with open(filename, mode='r') as f:
        return json.load(f)
