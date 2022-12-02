#!/usr/bin/python3
from sys import argv

print("1 argument.") if len(argv) == 2 else print(f"{len(argv)-1} arguments.")

for i in range(len(argv)):
    if i == 0:
        continue
    print(f"{i}: {argv[i]}")