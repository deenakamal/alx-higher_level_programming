#!/usr/bin/python3
""" Using GitHub API to display GitHub ID"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)

    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
