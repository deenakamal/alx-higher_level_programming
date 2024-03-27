#!/bin/bash
# Take URL then send a request and display the size.
curl -s "$1" | wc -c
