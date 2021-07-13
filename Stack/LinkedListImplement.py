class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Mystack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.value
    
    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1

        return self
    
    def pop(self):
        if self.top is None:
            print('Stack is empty')
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None

        return self

    def print_stack(self):
        if self.top is None:
            print('Stack empty')
        else:
            current_node = self.top
            while(current_node != None):
                print(current_node.value)
                current_node = current_node.next
        print()

my_stack = Mystack()
print(my_stack.peek())
#None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
#discord
#udemy
#google

print(my_stack.top.value)
#discord

print(my_stack.bottom.value)
#google

my_stack.pop()
my_stack.print_stack()
#udemy
#google

my_stack.pop()
my_stack.pop()
my_stack.print_stack()