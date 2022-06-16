def BinaryTree(r):
    return [r, [], []]


def insertLeft(root: list, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root: list, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root: list):
    return root[0]


def setRootVal(root: list, newVal) -> None:
    root[0] = newVal


def getLeftChild(root: list):
    return root[1]


def getRightChild(root: list):
    return root[2]


def main() -> None:
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    l = getLeftChild(r)
    print(l)
    setRootVal(l, 9)
    print(r)
    insertLeft(l, 11)
    print(r)
    print(getRightChild(getRightChild(r)))


if __name__ == "__main__":
    main()
