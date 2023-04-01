#!/bin/bash
# cURL 3
curl -sI $1 | grep 'Allow: ' | sed -e 's/Allow: //g'
