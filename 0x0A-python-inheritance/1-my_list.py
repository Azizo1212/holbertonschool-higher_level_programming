#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """prints the list sorted """

    def print_sorted(self):
        print(sorted(self))
