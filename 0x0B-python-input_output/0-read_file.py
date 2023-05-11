#!/usr/bin/python3
"""rwwedas"""

def read_file(filename=""):
    """reads a file"""
    with open(filename, "r", encoding="UTF-8") as f:
        f.read()
