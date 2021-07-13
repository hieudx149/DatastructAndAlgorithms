class hash_table:
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size

    def __str__(self): # As in the array implementation, this method is used to print the attributes of the class object in a dictionary format
        return str(self.__dict__)
    
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
             hash = (hash + ord(key[i])*i) % self.size
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = [[key, value]]
        else:
            self.data[address].append([key, value])
        print(self.data)

    def get(self, key):
        address = self._hash(key)
        bucket = self.data[address]
        if bucket:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        return None

    def keys(self):
        list_key = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    list_key.append(self.data[i][j][0])
        return list_key
    
    def values(self):
        list_value = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    list_value.append(self.data[i][j][1])
        return list_value

new_hash = hash_table(5)
new_hash.set('duong', 100)
new_hash.set('xuan', 200)
new_hash.set('hieu', 300)
print(new_hash.keys())
print(new_hash.values())