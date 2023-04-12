#!/usr/bin/python3
"""writes a string"""



def write_file(filename="", text=""):
    """writes a string"""
    with open(filename, mode = 'w', encoding='utf-8')as f:
        f.write(text)
        f.write(len(text))
