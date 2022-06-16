from Deque import Deque

d = Deque()
print(d.isEmpty())
d.addRear(4)
d.addFront(True)
print(d.size)
print(d.isEmpty())
d.addFront(8.4)
print(d)
print(d.removeRear())
print(d.removeFront())
print(d.size())
print(d)
