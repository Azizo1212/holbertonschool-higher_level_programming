#!/usr/bin/python3
"""Module 100-my_int"""


class MyInt(int):
    """Class inheriting from int"""

    def __eq__(self, x):

        return super().__ne__(x)

    def __ne__(self, x):

        return super().__eq__(x)
