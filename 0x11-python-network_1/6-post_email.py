#!/usr/bin/python3
"""
script that takes in a URL and an email address
sends a POST request to the passed URL 
"""

import requests, sys

if __name__ == "__main__":
    value = {"email":sys.argv[2]}
    req = requests.post(sys.argv[1], data=value)
    print(req.text)
