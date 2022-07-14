#!/usr/bin/python3
"""takes in a letter and sends a POST request"""

import requests
import sys


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        jresponse = response.json()
        if jresponse == {}:
            print("No result")
        else:
            ___id = jresponse['id']
            ___name = jresponse['name']
            print("[{}] {}".format(___id, ___name))
    except Exception:
        print("Not a valid JSON")
