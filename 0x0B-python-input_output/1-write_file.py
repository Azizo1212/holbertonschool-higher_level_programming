#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """ returns the number of characters written """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
