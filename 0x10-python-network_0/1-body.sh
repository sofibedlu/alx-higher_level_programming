#!/bin/bash
#script that takes in a URL, sends a GET request to the URL, and displays the body of 200 staus ./ code response
curl -sI "$1" | grep -q "HTTP/1.1 200 OK" && curl -s "$1"
