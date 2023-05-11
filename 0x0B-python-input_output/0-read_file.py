#!/usr/bin/python3
"""rwwedas"""

def read_file(filename=""):
    """reads a file"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
