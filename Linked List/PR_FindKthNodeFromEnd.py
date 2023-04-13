"""
LL: Find Kth Node From End (⚡Interview Question)

Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.

For example, let's say you want to find the item that is 3 steps away from the end of the LL. 
To do this, you would start from the head of the LL and move through the links until you reach the item that is 3 steps away from the end.

This is the problem of finding the "kth node from the end" of a linked list. 
Your task is to write a program that takes as input a linked list and a number k, and returns the item that is k steps away from the end of the list. If the linked list has fewer than k items, the program should return None.
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
  
  
#Solution in O(n)    
def find_kth_from_end(my_linked_list,k):
    # Initialize both slow and fast pointers to 
    # the head node of the linked list
    fast = my_linked_list.head
    slow = my_linked_list.head

    # Move the fast pointer k nodes ahead of the slow pointer
    # If fast pointer reaches the end (None) before k nodes, 
    # the linked list is too short and kth node doesn't exist
    for _ in range(k):
        if fast is None:
          fast = fast.next
        fast = fast.next

    # Move both pointers one node at a time until the fast 
    # pointer reaches the end of the linked list (None).
    # The slow pointer will now be pointing at the kth node 
    # from the end of the linked list.
    while fast is not None:
        slow = slow.next
        fast = fast.next
    
     # Return the kth node from the end of the linked list
    return slow

"""
SOLUTION
The find_kth_from_end function takes two parameters: a linked list called ll, and an integer k representing the index of the element to find from the end of the list.
The function initializes two pointers, slow and fast, to the head node of the linked list. 
The fast pointer is then moved k nodes ahead of the slow pointer. 
If the fast pointer reaches the end of the linked list before it moves k nodes, that means the linked list is too short to find the kth node from the end of the list, so the function returns None.
Otherwise, the slow and fast pointers are moved one node at a time until the fast pointer reaches the end of the linked list. 
The slow pointer will then be pointing at the kth node from the end of the linked list, so the function returns that node.
This function has a time complexity of O(n) where n is the length of the linked list

"""

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
