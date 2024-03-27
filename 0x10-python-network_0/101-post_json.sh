#!/bin/bash
# a bash script sends JSON POST request then displays response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
