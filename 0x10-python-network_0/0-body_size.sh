#!/bin/bash
# cURL body size
curl -I -s $1 | sed -n 's/Content-Length: //p'
