#!/usr/bin/python3
"""fetch X-Request-Id from header response"""

import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        str = response.headers.get('X-Request-Id')
        print(str)
