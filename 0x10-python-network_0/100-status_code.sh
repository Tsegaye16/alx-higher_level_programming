#!/bin/bash
# Sends a GET request to a given URL.
curl -s -o /dev/null -w "%{http_code}" "$1"
