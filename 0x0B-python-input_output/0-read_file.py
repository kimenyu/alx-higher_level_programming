#!/usr/bin/python3

""" 
A fuction that reads a  text file
"""

def read_file(filename=""):
    with open (filename, "r", encoding="UTF-8") as myFile:
        print(myFile.read(), end="")
