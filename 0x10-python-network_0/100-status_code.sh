#!/bin/bash
# script form pritig status code

curl -s -w "%{http_code}\n" "$1" -o /dev/null
