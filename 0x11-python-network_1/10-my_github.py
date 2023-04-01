#!/usr/bin/python3
"""script that takes GitHub credentials (username and password)
    and uses the GitHub API to display user id
   -in this we use personal access token as passwd
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    user = sys.argv[1]
    pat = sys.argv[2]
    authontication = HTTPBasicAuth(user, pat)
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=authontication)
    print(r.json().get('id'))
