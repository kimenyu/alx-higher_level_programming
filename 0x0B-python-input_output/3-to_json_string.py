#!/usr/bin/python3
"""returns json representation"""
import json


def to_json_string(my_obj):
	"""returns json str"""
	json_string = json.dumps(my_obj)
	return json_string
