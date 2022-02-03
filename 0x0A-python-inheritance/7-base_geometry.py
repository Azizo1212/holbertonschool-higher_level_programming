#!/usr/bin/python3
""" Module 7-base_geometry."""


class BaseGeometry():
    """Class with public instance method"""

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))

        elif value <= 0:
            raise TypeError('{} must be greater than 0'.format(name))
        else:
            self.value = value
