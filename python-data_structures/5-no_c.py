#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord("c"): None for in my_string})
    return new_string
