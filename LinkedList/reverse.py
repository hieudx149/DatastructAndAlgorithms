from Imp import myLinkedList

def reverse(linked_list):
    if linked_list.length <= 1:
        return linked_list.head
    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None
        linked_list.head = first
        return linked_list
        
new_LinkedList = myLinkedList(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.append(20)
new_LinkedList.insert(2, 15)
new_LinkedList = reverse(new_LinkedList)
new_LinkedList.print_linkedList()