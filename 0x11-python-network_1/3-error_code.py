#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8)
   -manage urllib.error.HTTPError exceptions and print:
    Error code: followed by the HTTP status code
"""
from urllib.error import HTTPError
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
