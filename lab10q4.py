from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes: Optional[Node] = None):
        if not nodes:
            self.head = None
            return
        self.head = Node(nodes[0])
        ptr: Node = self.head
        for x in nodes[1:]:
            ptr.next = Node(x)
            ptr = ptr.next
    def __repr__(self) -> str:
        node: Optional[Node] = self.head
        nodes: list = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def __iter__(self) -> str:
        node: Optional[Node] = self.head
        while node is not None:
            yield node
            node = node.next
    def add_last(self, node: Node):
        ptr: Optional[Node] = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = node

