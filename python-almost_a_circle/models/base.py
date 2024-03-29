#!/usr/bin/python3
"""This is class base"""


class Base:
    """initialize empty class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
