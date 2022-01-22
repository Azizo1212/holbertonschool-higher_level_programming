#!/usr/bin/python3
class Square:
    """Represents a square.
    Private instance attribute
    """

    def __init__(self, size=0):
        """class Square."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
