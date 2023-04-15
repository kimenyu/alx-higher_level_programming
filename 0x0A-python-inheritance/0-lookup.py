#!/usr/bin/python3
"""Returns the list of attributes"""



def lookup(obj):
    """returns attributes"""
    print( [i for i in dir(obj)])
