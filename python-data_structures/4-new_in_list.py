#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if idx > ((len(my_list)) - 1):
        return my_list
    elif idx < 0:
        return my_list
    elif idx in range(0, (len(my_list) - 1)):
        my_list[idx] = new_element
        return my_list
