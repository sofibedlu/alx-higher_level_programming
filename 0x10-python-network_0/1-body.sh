#!/bin/bash
#script that takes in a URL, sends a GET request to the URL, and displays the body of 200 staus ./ code response
curl -sfL "$1"
