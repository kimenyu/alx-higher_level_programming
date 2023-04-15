#!/usr/bin/python3
"""return true if inherited directly or indirectly"""



def inherits_from(obj, a_class):
    """returns true"""
    if issubclass (type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
