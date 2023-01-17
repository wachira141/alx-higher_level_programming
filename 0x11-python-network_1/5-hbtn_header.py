#!/usr/bin/python3
"""
Python script that takes in a URL
sends a request to the URL 
"""
import requests, sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))