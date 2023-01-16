#!/usr/bin/python3

""" load_from_json_file function """

import json


def load_from_json_file(filename):
	"""
	This function loads from a json file

	:param filename: string (JSON file)

	:return: Python object
	"""

	with open(filename, "r") as f:
		return json.loads(f.read())
