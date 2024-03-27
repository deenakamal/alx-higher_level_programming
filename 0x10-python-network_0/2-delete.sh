#!/bin/bash
#sends a DELETE request to the URL passed as the first argument then displays.
curl -sLX DELETE "$1"
