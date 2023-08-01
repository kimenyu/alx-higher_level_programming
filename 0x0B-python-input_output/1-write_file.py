#!/usr/bin/python3
"""writes a string"""


def write_file(filename="", text=""):
	"""writes"""
	with open(filename, 'w', encoding='utf-8') as f:
		return f.write(text)
