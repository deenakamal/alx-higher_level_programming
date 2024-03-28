#!/usr/bin/python3
""" take url, send request and display variable X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    print(response.headers.get("X-Request-Id"))
