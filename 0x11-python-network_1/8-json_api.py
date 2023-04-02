#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        jre = r.json()
        if not jre:
            print('No result')
        else:
            print("[{}] {}".format(jre.get('id'), jre.get('name')))
    except Exception:
        print('Not a valid JSON')
