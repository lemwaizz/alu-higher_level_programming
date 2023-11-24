#!/usr/bin/python3
"""returns list of available attributes and methods
"""


def lookup(obj):
    """using dir function"""
    return list(dir(obj))
