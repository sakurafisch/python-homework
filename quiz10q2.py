from typing import Optional
from __future__ import annotations

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
    def __repr__(self):
        return self.data
class LinkedList:
    def __init__(self, nodes=None):
        self.head: Node = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    # add an item to the last position in the Linked List.
    def add_last(self, node):
      # add your code here
        node_temp = self.head
        if node_temp is not None:
            while node_temp.next is not None:
                node_temp = node_temp.next
        node_temp.next = node
    def insert_after(self, node, item):
        tmp = node.next
        node.next = Node(item)
        node.next.next = tmp
    def delete_item(self, item):
        if not self.head:
            return
        if self.head.data == item:
            self.head = self.head.next
            return
        ptr: Node = self.head
        while (ptr):
            if ptr.data == item:
                ptr.next = ptr.next.next
                return
            ptr = ptr.next
            
       
def main() -> None:
    pass

if __name__ == '__main__':
    main()