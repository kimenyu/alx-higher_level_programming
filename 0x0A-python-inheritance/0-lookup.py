#!/usr/bin/python3
"""Returns the list of attributes"""



def lookup(obj):
    """returns attributes"""
    return [i for i in dir(obj)]
