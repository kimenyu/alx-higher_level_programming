#!/usr/bin/python3
"""reads a file"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        #read_file = f.read()
        #print(read_file, end="")
        for line in f:
            print(line, end="")
