#!/usr/bin/python3


import sys, requests

if __name__ == "__main__":
    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]
    ))

    data = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(data[i].get('sha'), data[i].get("commit").get('author').get("name")))
    except IndexError:
        pass
