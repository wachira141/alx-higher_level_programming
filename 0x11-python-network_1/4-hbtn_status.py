#!/usr/bin/python3
"""script to fetch from
    https://alx-intranet.hbtn.io/status
"""

import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    print("Body response:$")
    print("\t- type: {}".format(type(req.text)))
    print("\t- type: {}".format(req.text))