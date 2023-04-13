"""
LL: Has Loop (⚡Interview Question)
Write a method to determine if the Linked List contains a loop.

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
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    #Solution solved in O(n)
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
                
"""
SOLUTION
In this code, the has_loop method uses two pointers to traverse the linked list: slow and fast. 
The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. 
If there is a loop in the linked list, the slow and fast pointers will eventually meet, and the method will return True.
If there is no loop in the linked list, the fast pointer will eventually reach the end of the list, and the method will return False.

"""
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True



my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
