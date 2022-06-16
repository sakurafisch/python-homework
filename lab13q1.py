def BinaryTree(r) -> list:
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

#  left node <--(key)--> right node  
# For example, a node "a" has "b" as the left node and "c" as the right node.
# The output is "b <--(a)--> c". 

def BinaryTree_str(root: list) -> str:
    ans: str = ""
    if getLeftChild(root):
        ans = ans + str(getRootVal(getLeftChild(root)))
    else: 
        ans = ans + "None"
    ans = ans +  " <--("
    ans = ans + str(getRootVal(root))
    ans = ans + ")--> "
    if getRightChild(root):
        ans = ans + str(getRootVal(getRightChild(root)))
    else: 
        ans = ans + "None"
    return ans

	
r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)
setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
print(BinaryTree_str(r))
print(BinaryTree_str(getRightChild(r)))


# def BinaryTree(r):
#     return [r, [], []]
# def insertLeft(root,newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch, [], []])
#     return root
# def insertRight(root,newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch,[],[]])
#     return root
# def getRootVal(root):
#     return root[0]

# def setRootVal(root,newVal):
#     root[0] = newVal

# def getLeftChild(root):
#     return root[1]

# def getRightChild(root):
#     return root[2]
# def BinaryTree_str(root):
#     r = root[0]
#     lt = getLeftChild(root)
#     rt = getRightChild(root)
#     lt_r = None
#     rt_r = None
#     if lt:
#         lt_r = lt[0]
#     if rt:
#         rt_r = rt[0]
#     return f"{lt_r} <--({r})--> {rt_r}"

