#!/usr/bin/python3
"""
ython script that takes in a URL
sends a request to the URL and displays the
 value of the X-Request-Id
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as f:
        # content = f.read()
        print(dict(f.headers).get("X-Request-Id"))
