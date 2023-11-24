#!/usr/bin/python3
''' returns object (Python data structure) represented by a JSON string:'''


import json


def save_to_json_file(my_obj, filename):
    ''' returns saves to json file'''
    with open(filename, "w+") as f:
        return json.dump(my_obj, f)
