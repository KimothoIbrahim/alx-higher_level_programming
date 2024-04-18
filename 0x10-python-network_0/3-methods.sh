#!/bin/bash
#Display all allowed HTTP verbs
val=$(curl -s -i -X OPTIONS "$1" | grep Allow | sed s/"Allow: "//)
echo "$val"
