class Queue:
    def __init__(self) -> None:
        self.items: list = []

    def isEmpty(self) -> bool:
        return self.items == []

    def enqueue(self, item) -> None:
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        out = ""
        for i in self.items:
           out= out + str(i) +", "
        out =out[:-2] 
        return "Queue(["+ " " + out + "])"
    
    def exportToList(self) -> list:
        return self.items
