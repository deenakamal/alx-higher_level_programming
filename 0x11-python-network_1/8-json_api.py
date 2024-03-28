#!/usr/bin/python3
"""take letter and send POST request"""
import requests
import sys


if __name__ == "__main__":
    paramter = ""
    if len(sys.argv) > 1:
        paramter = sys.argv[1]
    data = {"q": paramter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get("id"),
                                   json_response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
