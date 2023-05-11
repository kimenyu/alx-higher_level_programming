#!/usr/bin/python3
"""writing"""


def write_file(filename="", text=""):
    """weriting"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
