#!/usr/bin/python3
"""Module 4-inherits_from"""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that inherited"""

    return isinstance(obj, a_class) and type(obj) != a_class
