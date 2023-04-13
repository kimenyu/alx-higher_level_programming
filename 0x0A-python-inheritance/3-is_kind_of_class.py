#!/usr/bin/python3
"""Returns True or false"""


def is_kind_of_class(obj, a_class):
    """Retuens True or false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
