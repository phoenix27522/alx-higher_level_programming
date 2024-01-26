#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

# Use a with statement to open the URL
with urllib.request.urlopen(url) as response:
    # Read the content of the response
    content = response.read().decode('utf-8')

    # Display the body of the response
    print(f"Body response:\n\t- type: {type(content)}\n\t- content: {content}")
