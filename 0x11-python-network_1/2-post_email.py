#!/usr/bin/python3
""" take url send a POST request with email"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('utf-8')
    with urlopen(url, data) as response:
        body = response.read()
     print(body.decode("utf-8"))
