#!/usr/bin/python3
""" class Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)

    def area(self):
        """Computes the area of the Rectangle instance"""

        return self.__width * self.__height

    def __str__(self):
        """Rectangle Descreption"""

        return("[Rectangle] {}/{}".format(self.__width, self.__height))
