#!/bin/bash
#send json post
curl -s -d @$2 -X POST "$1" -H "Content-Type: application/json"
