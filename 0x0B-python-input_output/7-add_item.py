#!/usr/bin/python3
"""importing system module"""


import sys
"""importing save_to_json_file module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""importing load_from_json_file"""


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = list(sys.argv[1:])

save_to_json_file(my_list, "add_item.json")
load_from_json_file("add_item.json")
