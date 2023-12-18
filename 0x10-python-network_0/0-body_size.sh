#!/bin/bash
# curl the argument provided as host and display body size
curl -s $1 -w "%{size_download}\n" -o /dev/null
