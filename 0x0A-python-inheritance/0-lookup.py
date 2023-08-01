#!/usr/bin/python3
"""function that returns the list of available attributes and methods of an object:"""

def lookup(obj):
	"""returns"""
	return [attr for attr in dir(obj) if not attr.startswith('__')]
