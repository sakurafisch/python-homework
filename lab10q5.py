from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    # the overload construction method that adds an array of items into the Doubly Linked List.
    def __init__(self, nodes: Optional[list] = None):
        if not nodes or nodes == []:
            self.head = None
            return
        self.head: Node = Node(nodes[0])
        ptr: Node = self.head
        for x in nodes[1:]:
            ptr.next = Node(x)
            ptr.next.previous = ptr
            ptr = ptr.next

    def __repr__(self):
        node: Optional[Node] = self.head
        nodes = []
        revnodes = []
        while node is not None:
            nodes.append(node.data)
            prenode = node.previous
            node = node.next
            if prenode is not None:
                revnodes.append(prenode.data)
            else:
                revnodes.append("None")
            if node is None:
                revnodes.append(prenode.next.data)
               # last not of the reversed order
        nodes.append("None")
        return "Next: " + " -> ".join(nodes) + " | Previous: " + " <- ".join(revnodes)
