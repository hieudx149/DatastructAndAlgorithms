class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None
class Double_LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.value, end= ' ')
                current_node = current_node.next
        print()

    def append(self, value):
        newNode = Node(value)
        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

        return self.print_list()
    
    def prepend(self, value):
        newNode = Node(value)
        self.head.previous = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1

        return self.print_list()

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            newNode = Node(value)
            current_node.next.previous = newNode
            newNode.next = current_node.next
            newNode.previous = current_node
            current_node.next = newNode
        self.length += 1
        return self.print_list()
    
    def remove(self, index):
        current_node = self.head
        if index == 0:
            current_node.next.previous = None
            self.head = current_node.next
        elif index == self.length-1:
            for _ in range(index-1):
                current_node = current_node.next
            current_node.next = None
        else:
            for _ in range(index-1):
                current_node = current_node.next
            current_node.next.next.previous = current_node
            current_node.next = current_node.next.next

        return self.print_list()

new_double_linkedlist = Double_LinkedList(10)
new_double_linkedlist.append(20)
new_double_linkedlist.append(20)
new_double_linkedlist.append(40)
new_double_linkedlist.insert(1, 15)
new_double_linkedlist.remove(1)