#!/usr/bin/python3
"""class that inherits from built in list class"""


class MyList(list):
    """class that inherits from list
    """

    def print_sorted(self):
        """sorts list"""
        sorted_list = self[:].sort()
        return sorted_list
