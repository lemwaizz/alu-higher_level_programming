#!/usr/bin/python3
def element_at(my_list, idx):
    for item in my_list:
        idx = input("idx = ")
        my_list = list(input("my_list = "))
        if idx < 0:
            return None
        elif idx >= len(my_list):
            return None
        else:
            print("Element at index {:d} is {}".format(my_list[idx], idx))
