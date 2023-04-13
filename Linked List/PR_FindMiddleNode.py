"""
LL: Find Middle Node (⚡Interview Question)
Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.

"""

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
    
    #Solution solved in O(n)
    def find_middle_node(self):
      slow = self.head
      fast = self.head

      while fast is not None and fast.next is not None:
          slow = slow.next
          fast = fast.next.next
      return slow
          
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )


""""
SOLUTION 
This method (find_middle_node) uses two pointers, slow and fast, and advances them at different speeds through the list. 
The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. 
By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

"""

"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""