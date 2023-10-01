#!/bin/bash
# Sends a JSON POST request to a given URL.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
