class MyStack:
    def __init__(self) -> None:
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]
    
    def push(self, value):
        self.array.append(value)
        return self
    
    def pop(self):
        newArray = self.array[:-1]
        self.array = newArray
        
        return self

    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])

        print('\n')

my_stack = MyStack()
my_stack.push("Duong")
my_stack.push("Xuan")
my_stack.push("Hieu")
my_stack.push("Pro")
my_stack.pop()
my_stack.print_stack()
print(my_stack.peek())