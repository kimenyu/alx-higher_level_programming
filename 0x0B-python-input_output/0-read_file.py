#!/usr/bin/python3
"""a function that reads a file"""


def read_file(filename=""):
	"""use the with statement"""
	with open(filename, 'r', encoding="utf-8") as f:
		for line in f:
			print(line, end="")
