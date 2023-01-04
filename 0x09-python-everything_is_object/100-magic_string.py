#!/usr/bin/python3
def magic_string():
    magic_string.n += 1
    return "BestSchool, " * magic_string.n + "BestSchool"
magic_string.n = -1
