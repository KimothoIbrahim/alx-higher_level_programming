#!/bin/bash
#send a cookie
curl -s -X GET "$1" -H "X-School-User-Id: 98"
