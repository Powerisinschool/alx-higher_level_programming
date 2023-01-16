#!/usr/bin/python3

""" This is read_file function """


def read_file(filename=""):
	"""
	This function reads a file
	"""
	with open(filename, "r") as f:
		print(f.read())
