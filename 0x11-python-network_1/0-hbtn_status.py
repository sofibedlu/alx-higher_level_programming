#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
                as re:
            content = re.read()
            utf = content.decode('utf-8')
            print("Body response:")
            print("     - type: {}".format(type(content)))
            print("     - content: {}".format(content))
            print("     - utf8 content: {}".format(utf))
    except urllib.error.URLError as e:
        print(e.reason)
