#!/usr/bin/python3

""" write_file function """


def write_file(filename="", text=""):
	""" This function writes a given string to the file specified """
	with open(filename, "w") as f:
		return f.write(text)
	