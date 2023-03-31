#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of
    the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    value = urllib.parse.urlencode(value)
    data = value.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
