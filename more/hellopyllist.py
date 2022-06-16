import pyllist

d = pyllist.sllist([1,2,3,4,5,6,4,7])
print(d)
print(d[0])
print("-----")
for i in d:
    print(i, end=",")
print("")
print("----")
node = d.first
node = node.next
print(node)
print(node.value)
print(node.next)
print(node.list)
print(d.size)
d.insert(5)
d.appendleft(11)
d.appendright(12)
d.insertafter(node, 10)
print(d)
