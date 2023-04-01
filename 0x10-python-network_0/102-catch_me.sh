#!/bin/bash
# Script to bypass local HTTP protocol using cURL
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me
