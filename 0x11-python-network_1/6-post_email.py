#!/usr/bin/python3
"""
script that takes in a URL and an email address
sends a POST request to the passed URL 
with the email as a parameter
finally displays the body of the response.
"""

import requests, sys

if __name__ == "__main__":
    value = {"email":sys.argv[2]}
    req = requests.post(sys.argv[1], data=value)
    print(req.text)
