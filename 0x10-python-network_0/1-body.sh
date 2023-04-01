#!/bin/bash

url=$1
response=$(curl -L -s -w "\n%{http_code}" $url)
body=$(echo "$response" | head -n1)
status=$(echo "$response" | tail -n1)

if [ "$status" == "200" ]; then
  echo "$body"
else
  echo "Request failed with status code $status"
fi
