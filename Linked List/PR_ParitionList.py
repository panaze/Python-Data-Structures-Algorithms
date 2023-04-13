"""
LL: Partition List (⚡Interview Question)
You are given a singly linked list implementation in Python that does not have a tail pointer (which will make this method simpler to implement).
You are tasked with implementing a method partition_list(self, x) that will take an integer x and partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. 
You should preserve the original relative order of the nodes in each of the two partitions.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #Solution solved in O(n)
    def partition_list(self,x):
        
        # If linked list is empty, return None
        if self.head is None:
          return None
        
        #Create two lists one for elements less than x and one for elements greater thanx
        llmin = LinkedList(0)
        dummy1 = llmin.head
        llmay = LinkedList(0)
        dummy2 = llmay.head
        
        
        #Add elements of original list to two new lists
        current = self.head
        while current is not None:
            if current.value < x:
                llmin.append(current.value)
            else:
                llmay.append(current.value)
            current = current.next

        #Eliminate dummy nodes from the two completed lists
        llmin.head = dummy1.next
        llmay.head = dummy2.next

        #Make the original list head be the list with elements smaller than x
        self.head = llmin.head

        #Get the tail of list with elements smaller than x
        tail = self.head
        while True:
            if tail.next is None:
                break
            tail = tail.next

        #Connect the tail of smaller list to head of the list with greater elements
        tail.next = llmay.head
            

        
"""
SOLUTION:
Create two lists one for elements less than x and one for elements greater than x.
Add elements of original list to two new lists.
Eliminate dummy nodes from the two completed lists.
Make the original list head be the list with elements smaller than x.
Get the tail of list with elements smaller than x.
Connect the tail of smaller list to head of the list with greater elements.
"""
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""