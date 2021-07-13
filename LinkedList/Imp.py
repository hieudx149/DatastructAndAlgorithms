
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class myLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

        return self
    
    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

        return self

    def print_linkedList(self):
        
        current_node = self.head
        while current_node!= None:
            print(current_node.value, end= ' ')
            current_node = current_node.next
            
    def insert(self, index, value):

        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            print("can't add new node, out of range !")
        else:
            newNode = Node(value)
            current_node = self.head
            for i in range(0, index-1):
                current_node = current_node.next
            newNode.next = current_node.next
            current_node.next = newNode
            self.length += 1
        return self.print_linkedList()
    
    def remove(self, index):

        current_node = self.head
        if index == 0:
            self.head = current_node.next
        elif index == self.length-1:
            for _ in range(index-1):
                current_node = current_node.next
            current_node.next = None
        else:
            for _ in range(index-1):
                current_node = current_node.next
            next_node = current_node.next.next
            current_node.next = next_node
        self.length -= 1
        return self.print_linkedList()

# new_linked_list = myLinkedList(10)
# new_linked_list.append(20)
# new_linked_list.prepend(5)
# new_linked_list.insert(2, 7)
# new_linked_list.print_linkedList()
# print('\n')
# new_linked_list.remove(3)
# new_linked_list.print_linkedList()