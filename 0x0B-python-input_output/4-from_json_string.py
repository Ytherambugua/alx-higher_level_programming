#!/usr/bin/python3
''' function that returns an object(Python data structure) represented by JSON string'''

import json

def from_json_string(my_str):
    '''from json string'''
    return json.loads(my_str)
