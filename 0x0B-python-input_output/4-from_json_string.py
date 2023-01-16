#!/usr/bin/python3

""" from_json_string function """

import json


def from_json_string(my_str: str) -> dict:
	"""
	This function converts a json string to a python object(dictionary)

	:param my_str: json_tring
	:return: python object (dictionary)
	"""
	return json.loads(my_str)
