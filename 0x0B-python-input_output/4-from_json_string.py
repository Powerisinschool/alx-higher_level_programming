#!/usr/bin/python3

""" from_json_string function """

import json


def from_json_string(my_str: str) -> dict:
	"""
	This function converts a string to a python object
	"""
	return json.loads(my_str)
