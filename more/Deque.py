class Deque:
    def __init__(self) -> None:
        self._items: list = []
    
    def isEmpty(self) -> bool:
        return self._items == []
    
    def addFront(self, item) -> None:
        self._items.append(item)

    def addRear(self, item):
        self._items.insert(0, item)
    
    def removeFront(self):
        return self._items.pop()

    def removeRear(self):
        return self._items.pop()
    
    def size(self) -> int:
        return len(self._items)
    
    def __str__(self) -> str:
        return f"Deque({self._items})"
