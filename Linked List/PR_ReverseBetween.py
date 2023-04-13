"""
LL: Reverse Between (⚡Interview Question)
You are given a singly linked list and two integers m and n. 
Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

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
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next   
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

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
    def reverse_between(self,m,n):
         # If the linked list is empty, then return None.
        if not self.head:
            return None
 
        # create a dummy node and connect it to the head.
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
 
        # move prev to the node at position m.
        for i in range(m):
            prev = prev.next
 
        # set current to the next node of prev.
        current = prev.next
    
        # Reverse the linked list from position m to n.
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
 
        # update the head of the linked list with the next node of the dummy.
        self.head = dummy.next


"""
SOLUTION
If the linked list is empty, the method returns None.
The method first creates a dummy node with value 0 and sets its next attribute to the head of the linked list. 
Then, it sets prev to the dummy node and iterates prev m times.
At this point, prev points to the node that precedes the m-th node.
Next, the method sets current to the m-th node and iterates through the linked list n-m times.
In each iteration, the method swaps the next pointers of current and its next node, thereby reversing the order of the nodes between positions m and n.
The method uses a temporary variable temp to store the next node of current, which is needed to perform the swap.
Finally, the method updates the head of the linked list to the next node of the dummy node.
"""
    



linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
