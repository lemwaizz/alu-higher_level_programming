#!/usr/bin/python3
''' returns object (Python data structure) represented by a JSON string:'''


import json


def from_json_string(my_obj):
    ''' returns a json obj'''
    return json.loads(my_obj)
