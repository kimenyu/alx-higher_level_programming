#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout:"""



def read_file(filename=""):
    """reads file"""
    with open(filename, mode = "r", encoding="UTF-8") as f:
        print(f.read(), end="")
