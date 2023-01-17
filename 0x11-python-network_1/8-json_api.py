#!/usr/bin/python3
import requests, sys

if __name__ == "__main__":
    letter = ''
    if len(sys.argv) > 1:
        letter = {'q':sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
    