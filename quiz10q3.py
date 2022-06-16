from typing import Optional
from __future__ import annotations

class Node:

    def __init__(self, data):

        self.data = data

        self.next: Optional[Node] = None

        self.previous: Optional[Node] = None

    def __repr__(self):

        return self.data

class DoublyLinkedList:

    def __repr__(self):

        node = self.head

        nodes = []

        revnodes = []

        while node is not None:

            nodes.append(node.data)

            prenode: Optional[Node] = node.previous

            node = node.next

            if prenode is not None:

                revnodes.append(prenode.data)

            else:

                revnodes.append("None")

            if node is None:

               revnodes.append(prenode.next.data)

               #last not of the reversed order

        nodes.append("None")

        return "Next: " + " -> ".join(nodes) + " | Previous: " +" <- ".join(revnodes)

        # the overload construction method that adds an array of items into the Doubly Linked List.

    def __init__(self, nodes = None):

        # add your code here

        self.head = None

        if nodes is not None:

            node = Node(data=nodes.pop(0))

        self.head = node

        pre_node = None

        for elem in nodes:

            node.next = Node(data=elem)

            pre_node = node

            node = node.next
            node.previous = pre_node
    def insert_before(self, node: Optional[Node], item):
        if self.head == node:
            tmp = Node(item)
            self.head.previous = tmp
            tmp.next = self.head
            self.head = tmp
            return
        t = node.previous
        node.previous = Node(item)
        node.previous.previous = t
        node.previous.next = node

