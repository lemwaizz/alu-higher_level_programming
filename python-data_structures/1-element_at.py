#!/usr/bin/python3
def element_at(my_list, idx):
    idx = range(0, (len(my_list) - 1))
    for item in my_list:
        if idx < 0:
            return None
        elif idx >= (len(my_list) - 1):
            return None
