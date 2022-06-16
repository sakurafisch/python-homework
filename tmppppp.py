class Stack:
    def __init__(self) -> None:
        self._items: list = []
    
    def isEmpty(self) -> bool:
        return self._items == []
    
    def push(self, item) -> None:
        return self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[len(self._items) - 1]
    
    def size(self) -> int:
        return len(self._items)
    
    def __str__(self) -> str:
        out: str = ""
        for i in self._items:
            out = out + str(i) + ", "
        out = out[:-2]
        return f"Stack([ {out} ])"


class Queue:
    def __init__(self) -> None:
        self._items: list = []

    def isEmpty(self) -> bool:
        return self._items == []
    
    def enqueue(self, item) -> None:
        self._items.insert(0, item)
    
    def dequeue(self):
        return self._items.pop()
    
    def size(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return f"Queue({self._items})"


stackObj1 = Stack()

stackObj2 = Stack()

queueObj = Queue()

for i in range(0, 5):

    queueObj.enqueue(i*2)

    queueObj.enqueue(i*2 + 1)

    stackObj1.push(queueObj.dequeue())

    stackObj2.push(queueObj.dequeue())

for i in range(0, 5):

    print(stackObj1.pop())

for i in range(0, 5):

    print(stackObj2.pop())