#!/usr/bin/python3
"""writes a string"""



def write_file(filename="", text=""):
    """writes a string"""
    with open(filename, mode = 'w', encoding='utf-8') as :
        f.write(text)
        f.close()
        print(text.len())
