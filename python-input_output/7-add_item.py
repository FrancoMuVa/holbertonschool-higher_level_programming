#!/usr/bin/python3
import sys
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

argc = len(sys.argv)
for i in range(1, argc):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, "add_item.json")
