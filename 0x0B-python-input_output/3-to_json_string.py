#!/usr/bin/python3

""" to_json_string function """

import json


def to_json_string(my_obj):
	"""
	This converts a python object to a json string
	"""
	return json.dumps(my_obj)
