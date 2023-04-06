#!/usr/bin/python3
"""
funcion that prints My name is <first name> <last name>

Args:

parameter 1: first_name
parameter 2: last_name
Both first_name and last_name must be strings

results:
The function should print My name is {first_name} {last_name}

Raise:
TypeError: First_name must be a string or last_name must be a string

"""
def say_my_name(first_name, last_name=""):
	if not isinstance(first_name, str):
		raise TypeError("first_name must be a string")
	if not isinstance(last_name, str):
		raise TypeError("last_name must be a string")
	return (f"My name is {first_name} {last_name}")
