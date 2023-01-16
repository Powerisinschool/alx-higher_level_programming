#!/usr/bin/python3

""" Add args to list """

import json
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fp = "add_item.json"

if not os.path.exists(fp):
	save_to_json_file(sys.argv[1:], fp)
	sys.exit(0)

try:
	arr = load_from_json_file(fp)
except json.decoder.JSONDecodeError as e:
	arr = []

arr += sys.argv[1:]
save_to_json_file(arr, "add_item.json")
