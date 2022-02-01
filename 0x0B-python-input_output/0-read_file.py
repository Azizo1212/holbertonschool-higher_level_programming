#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read file"""

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
