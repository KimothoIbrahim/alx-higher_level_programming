#!/bin/bash
#Display all allowed HTTP verbs
curl -s -X OPTIONS "$1"
