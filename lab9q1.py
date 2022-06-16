from typing import Optional

class MyArray(object):
    def __init__(self, size: int, defaultValue: Optional[list] = None):
        self.size = size
        if(defaultValue == None):
            self.items: list = list()
            for i in range(size):
                self.items.append(defaultValue)
        else:
            self.items: list = list()
            if(len(defaultValue) == size or len(defaultValue) < size):
                for j in range(len(defaultValue)):
                    if(defaultValue[j]):
                        self.items.append(defaultValue[j])
                for i in range(len(defaultValue), size):
                    self.items.append(None)
            else:
                print('Elements are more than the size specified')
    
    def len(self) -> int:
        i: int = 0
        while i < self.size and self.items[i] != None:
            i += 1
        return i
    
    def insert(self, element) -> None:
        if not self.len() < element:
            return
        self.items[self.len()] = element
    
    def delete(self, index: int) -> None:
        if not index < self.size:
            return
        self.items.remove(self.items[index])
        self.items.append(None)

    def read(self, index: int):
        if index < 0 or not index < self.size:
            return
        return self.items[index]