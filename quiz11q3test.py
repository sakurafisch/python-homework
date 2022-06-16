class HashTable:
    def __init__(self, data: dict, table_size: int=11):
        self.size: int = table_size
        self.slots: list = [None] * self.size
        self.data: list = [None] * self.size
        for k, v in data.items():
            self.put(k, v)

    def put(self,key,data):
        hash_value: int = self.hashfunction(key, len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
            return
        if self.slots[hash_value] == key:
            self.data[hash_value] = data
            return
        nextslot: int = self.rehash(hash_value, len(self.slots))
        while self.slots[nextslot] != None and self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot, len(self.slots))
            if hash_value == nextslot:
                return False
        if self.slots[nextslot] == None:
            self.slots[nextslot] = key
            self.data[nextslot] = data
            return
        self.data[nextslot] = data

    def hashfunction(self,key,size) -> int:
        return key%size

    def rehash(self,oldhash,size) -> int:
        return (oldhash+1)%size

    def get(self,key):
        startslot: int = self.hashfunction(key, len(self.slots))
        position: int = startslot
        while self.slots[position] != None:
            if self.slots[position] == key:
                return self.data[position]
            position = self.rehash(position, len(self.slots))
            if position == startslot:
                return None

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def remove(self, key) -> bool:
        startslot: int = self.hashfunction(key, len(self.slots))
        position: int = startslot
        while self.slots[position] != None:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
                return True
            positon = self.rehash(position, len(self.slots))
            if (position == startslot):
                return False
        return False

