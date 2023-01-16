#!/usr/bin/python3

""" append_write function """


def append_write(filename="", text=""):
	"""
	This function appends text to a file
	"""
	with open(filename, "a") as f:
		return f.write(text)
