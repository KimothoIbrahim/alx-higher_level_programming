#!/bin/env bash
# curl the argument provided as host and display body size

if [ $# -eq 1 ]; then
	curl -s $1 -w "%{size_download}\n" -o /dev/null
fi
