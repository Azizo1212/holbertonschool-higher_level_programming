#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body """

import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    if ((response.status_code >= 400) and (response.status_code <= 599)):
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
