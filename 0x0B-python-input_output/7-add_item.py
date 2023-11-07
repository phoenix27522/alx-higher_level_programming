#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json


def save_to_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_from_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


if __name__ == '__main__':
    data = load_from_json_file("add_item.json")
    data.extend(sys.argv[1:])
    save_to_json_file("add_item.json", data)
