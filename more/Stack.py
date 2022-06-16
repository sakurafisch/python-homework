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
