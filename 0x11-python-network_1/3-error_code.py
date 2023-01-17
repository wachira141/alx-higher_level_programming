#!/usr/bin/python3
"""
Python script that takes in a URL
ends a request to the URL 
"""
import urllib.request, sys
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))