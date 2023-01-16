#!/usr/bin/python3

""" save_to_json_file function """

import json


def save_to_json_file(my_obj, filename: str):
	"""
	This function writes an Object to a text file

	:param my_obj: python object
	:param filename: string
	"""

	with open(filename, "w") as f:
		f.write(json.dumps(my_obj))
