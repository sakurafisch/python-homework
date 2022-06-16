class Stack:
    def __init__(self, items = []):
        self.items: list = items

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self) -> int:
        return len(self.items)
    
    def __str__(self) -> str:
        out = ""
        for i in self.items:
            out = out + str(i) + ", "
        out = out[:-2]
        return "Stack([" + " " + out + "])"
    
    def pushAList(self, items: list):
        for x in items:
            self.items.append(x)
