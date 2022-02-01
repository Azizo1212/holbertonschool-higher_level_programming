#!/usr/bin/python3
"""class Node."""


class Node:
    """Represents Node"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data."""
        return self.__data

    @data.setter
    def data(self, value):

        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):

        """ get next_node attribute"""
        return self.__next_node

    @position.setter
    def next_node(self, value):
        if type(value) != Node or type(value) is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""class SinglyLinkedList."""


class SinglyLinkedList:
    """SinglyLinkedList"""

    def __init__(self):
        self.head = None

    def __str__(self):

        i = ""
        node = self.head
        while node:
            i += str(node.data)
            i += '\n'
            node = node.next_node
        return i[:-1]

    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new.next_node = node.next_node
        node.next_node = new
