#!/bin/bash
# a Bash script sends request and displays only status.
curl -so /dev/null -w "%{http_code}" "$1"
