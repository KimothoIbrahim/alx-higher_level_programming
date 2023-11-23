#!/usr/bin/python3
"""Script taking args into list and saves to JSON file"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file =\
        __import__("6-load_from_json_file").load_from_json_file

    file = "add_item.json"
    buffer = []

    try:
        buffer = load_from_json_file(file)

        for i in sys.argv:
            if i != sys.argv[0]:
                buffer.append(i)
    except FileNotFoundError:
        buffer = sys.argv[1:]

    save_to_json_file(buffer, file)
