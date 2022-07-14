#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""

from urllib import request
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
            print("Error code: {}".format(e.code))
