#!/usr/bin/env bash
  
set -o errexit

docker build --tag stackoverflow .
docker run -ti stackoverflow
