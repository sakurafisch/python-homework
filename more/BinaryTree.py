from __future__ import annotations

class BinaryTree:
    def __init__(self, rootObj) -> None:
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.leftChild = self.leftChild
            self.leftChild = tmp

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.rightChild = self.rightChild
            self.rightChild = tmp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self) -> BinaryTree:
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def main() -> None:
    r: BinaryTree = BinaryTree("a")
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    print(r.getRightChild())
