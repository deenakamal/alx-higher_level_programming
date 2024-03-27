#!/bin/bash
# a Bash script that sends a request and displays the body of the response
curl -sLX GET "$1" -H "X-School-User-Id: 98"
