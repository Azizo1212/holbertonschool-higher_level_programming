#!/usr/bin/python3
""" class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square """

    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        """Computes the area of a Square """

        return self.__size ** 2

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
