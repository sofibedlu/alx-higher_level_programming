#!/usr/bin/python3
"""ython script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the header
    of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(sys.argv[1])) as re:
        print(re.getheader('X-Request-Id'))
