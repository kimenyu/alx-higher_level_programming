#!/usr/bin/python3

""" 
A fuction that reads a  text file
"""

def read_file(filename=""):

    """
    Using with kyword
    """

    with open (filename, 'r', encoding="utf-8") as myFile:
        print(myFile.read(), end="")
