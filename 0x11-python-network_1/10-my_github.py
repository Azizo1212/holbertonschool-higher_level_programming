#!/usr/bin/python3
"""takes your GitHub credentials """

import requests
import sys


if __name__ == '__main__':
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    jresponse = response.json()
    try:
        print(jresponse['id'])
    except KeyError:
        print('None')
