#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = list(reversed(my_list))
    i = int(range(0, (len(new_list) - 1)))
    print("{:d}".format(new_list[i]), end='')
