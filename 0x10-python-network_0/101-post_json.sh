#!/bin/bash
# cURL POST JSON
curl -sX POST -H "Content-Type: application/json" -d @"$2" $1
