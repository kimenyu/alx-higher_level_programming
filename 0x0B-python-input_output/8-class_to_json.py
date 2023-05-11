#!/usr/bin/python3
"""class module"""
import json


def class_to_json(obj):
    """class"""

    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return obj
