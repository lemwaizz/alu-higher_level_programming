#!/usr/bin/python3
"""function to read utf8 file and print in stdout
"""


def read_file(filename=""):
    """read file function
    """
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
