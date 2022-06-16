class HashTable:
    def __init__(self, data, table_size=11):
        self.size = table_size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        for k, v in data.items():
            self.put(k, v)

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))  # slots[]'s index
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:  # already had the same key, so refresh data
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))  # slots[]'s index
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))  # slots[]'s index
                if hashvalue == nextslot:  # already traverse once
                    return False
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:  # self.slots[nextslot] = key
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        n = 0
        p = (oldhash + n * n) % size
        while True:
            if self.slots[p] == None:
                return p
            else:
                n += 1
                p = (p + n * n) % size
        return p

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))  # slots[]'s index
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def remove(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))  # slots[]'s index
        if self.slots[hashvalue] == None:
            return True
        else:
            if self.slots[hashvalue] == key:  # already had the same key, so refresh data
                self.slots[hashvalue] == None
                self.data[hashvalue] = None
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))  # slots[]'s index
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))  # slots[]'s index
                if hashvalue == nextslot:  # already traverse once
                    return False
                if self.slots[nextslot] == None:
                    return True
                else:  # self.slots[nextslot] = key
                    self.slots[nextslot] = None
                    self.data[nextslot] = None
                    return True