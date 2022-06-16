class Deque:
    def __init__(self):
        self.items: list = []

    def isEmpty(self) -> bool:
        return self.items == []

    def addFront(self, item) -> None:
        self.items.append(item)

    def addRear(self, item) -> None:
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        out: str = ""
        for i in self.items:
           out= out + str(i) +", "
        out =out[:-2] 
        return "Deque(["+ " " + out + "])"
    
    def emptyDeque(self) -> None:
        self.items.clear()
