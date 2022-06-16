from queue import Queue, LifoQueue
from collections import deque

q = Queue()
q.put("A")
q.put(10)
q.put("B")
print("---Queue---")
print(q.get())
print(q.get())
print(q.qsize())
s = LifoQueue()
s.put("A")
s.put(10)
s.put("B")
print("---Stack---")
print(s.get())
print(s.get())
print(s.qsize())
d = deque()
d.append("A")
d.append(10)
d.appendleft("B")
print("---Deque---")
print(d.pop())
print(d.popleft())
print(list(d))


