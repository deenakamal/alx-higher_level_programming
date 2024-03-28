#!/usr/bin/python3
""" script that lists 10 of last commits"""
import sys
import requests


if __name__ == "__main__":
    owner_name = sys.argv[1]
    repo_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        repo_name, owner_name)
    request = requests.get(url)
    number_of_commits = request.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                number_of_commits[i].get("sha"),
                number_of_commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
