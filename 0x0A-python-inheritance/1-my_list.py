#!/usr/python3
"""A class that inherits"""

class MyList(list):
    """Public instance method"""
    def print_sorted(self):
        print(sorted(self))
