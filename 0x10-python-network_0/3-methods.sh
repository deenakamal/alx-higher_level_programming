#!/bin/bash
# Takes in URL and displays all HTTP methods server.
curl -sIX OPTIONS $1 | grep Allow | cut -d' ' -f2-
