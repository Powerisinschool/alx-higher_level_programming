#!/usr/bin/python3

""" Class to JSON module """


def class_to_json(obj):
	"""
	This function returns the dictionary description of an object for JSON serialization

	:param obj: An instance of a class
	:return: dictionary description of the object
	"""

	return obj.__dict__
