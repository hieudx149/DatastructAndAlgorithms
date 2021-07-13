from typing import NewType


class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self) -> str:
        return str(self.__dict__)
    
    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        deletedItem = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1

        return deletedItem

newArrray = Array()
newArrray.push(10)
newArrray.push('hello')
print(newArrray.get(1))
print(newArrray)
print(newArrray.delete(0))
print(newArrray)
#print(newArrray)