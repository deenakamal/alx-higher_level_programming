#!/usr/bin/python3
"""take url & email then send a request"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    email = {"email": sys.argv[2]}
    response = requests.post(url, email).text
    print(response)
