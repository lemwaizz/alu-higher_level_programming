#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if idx > ((len(my_list)) - 1):
        return my_list
    elif idx < 0:
        return my_list
    else:
        new_list = my_list
        new_list[idx] = new_element
        return new_list
