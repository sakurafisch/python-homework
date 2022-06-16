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
