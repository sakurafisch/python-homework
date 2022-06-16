from typing import Optional
from __future__ import annotations

class TreeNode:
    def __init__(self,key,val,left: Optional[TreeNode] = None, right: Optional[TreeNode] = None, parent: Optional[TreeNode] = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                   if self.isLeftChild():
                       succ = self.parent
                   else:
                       self.parent.rightChild = None
                       succ = self.parent.findSuccessor()
                       self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __str__(self) -> str:
        ans = ""
        ans = ans + f"Node:[Key:{self.key},value:{self.payload}],Left Child:"
        if self.leftChild:
            ans = ans + f"[key:{self.leftChild.key},value:{self.leftChild.payload}],Right Child:"
        else:
            ans = ans + "None,Right Child:"
        if self.rightChild:
            ans = ans + f"[key:{self.rightChild.key},value:{self.rightChild.payload}],Parent:"
        else:
            ans = ans + "None,Parent:"
        if self.parent:
            ans = ans + f"[key:{self.parent.key},value:{self.parent.payload}]"
        else:
            ans = ans + "None"
        return ans

def main() -> None:
    a = TreeNode(1, "A")
    print(a)
    c = TreeNode(3, "C")
    d = TreeNode(4, "D")
    print(d)
    b = TreeNode(5, "B", a, c, d)
    print(b)

if __name__ == '__main__':
    main()
