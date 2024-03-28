#!/usr/bin/python3
""" take url sends a request to the URL then display the response"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.status))
