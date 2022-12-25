#!/usr/bin/python3
"""Define classes of Node and SinglyLinkedList"""


class Node:
    """represent node of linked list"""
    def __init__(self, data, next_node=None):
        """initialize node
        Args:
            data (int): int data of the list
            next_node (Node): next node of the list
            """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """to set data to the list"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """to retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """to set next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """represent singly linked list"""
    def __init__(self):
        """initiate the list"""
        self.__head = None

    def __str__(self):
        """print the singly list object members"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

    def sorted_insert(self, value):
        """that inserts a new Node into the correct
        sorted position in the list (increasing order)"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new
