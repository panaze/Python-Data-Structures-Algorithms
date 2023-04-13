"""
LL: Remove Duplicates (⚡Interview Question)
Remove all duplicates from the Linked List.

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

    #Solved in O(n)
    def remove_duplicates(self):
      current = self.head
      dictionary = {}
      before = None

      while current:
        if current.value in dictionary:
            before.next = current.next
            self.length -=1
        else:
            dictionary[current.value] = current.value
            before = current
        current = current.next

"""""
SOLUTION
In this implementation, the linked list is iterated over using a while loop, with the current variable starting at the head of the linked list and the previous variable starting at None. 
If the current node's value is in the dictionary, it's a duplicate, so the previous node's next attribute is set to the current node's next attribute. 
This effectively removes the duplicate node from the linked list. 
If the current node's value is not in the dictionary, it's added to the dictionary, and the previous variable is set to current. 
Finally, the current variable is set to the current node's next attribute, and the iteration continues until current is None.

"""


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    4
    
"""
