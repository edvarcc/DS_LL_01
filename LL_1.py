class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        
 def find_midle_node(self):                                   
    slow = self.head
    fast = self.tail      
    
INITIALIZE slow and fast pointers to head of the linked list

WHILE fast is not None and fast.next is not None:
    MOVE slow pointer one step (slow = slow.next)
    MOVE fast pointer two steps (fast = fast.next.next)

return slow



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )

