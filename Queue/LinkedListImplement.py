class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first.value
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.last is None:
            self.last = new_node
            self.first = self.last
            self.length += 1
            return 
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return
    
    def dequeue(self):
        if self.first is None:
            print('Queue is empty')
        if self.first == self.last:
            self.first = None
            self.last = None
        current_node = self.first.next
        self.first = current_node
        self.length -= 1
    
    def print_queue(self):
        if self.length == 0:
            print('Queue is empty')
        else:
            current_pointer = self.first
            while(current_pointer != None):
                if current_pointer.next == None:
                    print(current_pointer.value)
                else:
                    print(f'{current_pointer.value} <----', end=' ')
                current_pointer = current_pointer.next
        print('\n')
        
my_queue = MyQueue()
my_queue.enqueue("My")
my_queue.enqueue("name")
my_queue.enqueue("is")
my_queue.enqueue("Xuan Hieu")
my_queue.print_queue()
print(my_queue.peek())