#!/bin/bash
# cURL
curl -so /dev/null -w "%{http_code}" $1
