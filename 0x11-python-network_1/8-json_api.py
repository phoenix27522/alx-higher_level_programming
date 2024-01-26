#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
   with a letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    # Set the default value for the letter parameter
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Data to be sent in the POST request
    data = {'q': q}

    # Send a POST request to the specified URL with the letter parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        json_data = response.json()

        if json_data and isinstance(json_data, dict):
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
