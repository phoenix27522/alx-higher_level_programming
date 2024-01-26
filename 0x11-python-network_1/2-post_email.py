#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request

def send_post_request(url, email):
    # Prepare data for the POST request
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Create a POST request
    request = urllib.request.Request(url, data)

    # Send the POST request and handle the response
    with urllib.request.urlopen(request) as response:
        # Print the body of the response
        print(response.read().decode("utf-8"))

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    # Extract URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Send the POST request and display the response
    send_post_request(url, email)
