#!/usr/bin/env bash
# cURL body size
curl -I -s 0.0.0.0:5000 | sed -n 's/Content-Length: //p'
