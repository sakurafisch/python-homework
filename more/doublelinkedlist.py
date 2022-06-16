import pyllist

d = pyllist.dllist([1, 2, 3, 4, 5, 6, 4, 7])

print(d)
print(d[0])
print(d[1])
print("-----")
for i in d:
    print(i, end=",")
print("")
print("-----")
print(d.size)
print("""
search for node with value = 5 and add 10 after
the node before 5""")
for i in d.iternodes():
    if i.value == 5:
        d.insert(10, after=i.prev)
        # or d.insert(10, before=i)
print(d)
