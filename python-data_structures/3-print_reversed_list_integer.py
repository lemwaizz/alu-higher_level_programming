#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = list(reversed(my_list))
    for listmethod in new_list:
        for item in listmethod:
            print("{:d}".format(item))
