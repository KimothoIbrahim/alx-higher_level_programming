#!/bin/bash
#Display all allowed HTTP verbs
echo $(curl -s -i -X OPTIONS "$1" | grep Allow | sed s/"Allow: "//)
