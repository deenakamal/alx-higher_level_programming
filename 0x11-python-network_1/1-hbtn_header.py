#!/usr/bin/python3
""" take url, send request and display X-Request-Id variable """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
