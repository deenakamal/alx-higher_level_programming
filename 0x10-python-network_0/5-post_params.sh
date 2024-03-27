#!/bin/bash
# a Bash script that sends a POST rewuest and displays the response.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
