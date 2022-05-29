#!/usr/bin/python3
"""takes in a URL and an email"""

if __name__ == "__main__":

import urllib.request
import urllib.parse
import sys

    url = argv[1]
    value = {"email": sys.argv[2]}
    data = parse.urlencode({'email': email}).encode()
    str = request.Request(url=url, data=data)

    with request.urlopen(str) as response:
        print(response.read().decode('utf-8'))
