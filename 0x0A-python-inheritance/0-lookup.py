#!/usr/bin/python3
"""lookpu"""



def lookup(obj):
    """Return a list"""
    mydir = dir(obj)
    return list(mydir)
