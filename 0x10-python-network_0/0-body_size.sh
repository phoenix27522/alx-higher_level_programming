#!/bin/bash
# get the bite size of the http responce header
curl -s "$1" | wc -c