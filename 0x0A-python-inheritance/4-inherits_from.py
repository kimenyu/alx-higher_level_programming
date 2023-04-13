#!/usr/bin/python3
"""Returns True"""


def inherits_from(obj, a_class):
    """Returns True"""
    if issubclass(obj, a_class):
        return True
    else:
        return False
