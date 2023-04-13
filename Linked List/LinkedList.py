class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    #CONSTRUCTOR: Create a new linked list
    #Time Complexity: O(1)
    def __init__(self,value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1

    #PRINT_LIST: Print the list
    #Time Complexity: O(n)
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end = " ")
            if temp.next is not None:
              print("->" , end = " ")
            temp = temp.next

    #APPEND: Add a new node to the end of the list
    #Time Complexity: O(1)
    def append(self,value): 
        new_Node = Node(value)
        if self.head is None :
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length += 1
                #Optional
        return True
    
    #POP: Remove the last node from the list
    #Time Complexity: O(n)
    def pop(self):
        #Check if the list is empty
        if self.length == 0:
            return None
        #Create a temp variable to store the last node
        temp = self.head
        #Create a pre variable to store the node before the last node
        pre = self.head
        #Loop through the list until the last node
        while temp.next is not None:
          pre = temp
          temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        #Check if the list is empty after removing the last node
        if self.length == 0:
            self.head = None
            self.tail = None
        #Return the removed node
        return temp
    
    #PREPEND: Add a new node to the beginning of the list
    #Time Complexity: O(1)
    def prepend(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head = new_Node
        self.length += 1
        #Optional
        return True
    
    #POP_FIRST: Remove the first node from the list
    #Time Complexity: O(1)
    def pop_first(self):
        #Check if the list is empty
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        #Check if the list is empty after removing the first node
        if self.length == 0:
            self.tail = None
        #Return the removed node
        return temp
    
    #GET: Get the node at a specific index
    #Time Complexity: O(n)
    def get(self,index):
        #Check if the index is out of range
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
          temp = temp.next
        return temp
    
    #SET: Set the value of a node at a specific index
    #Time Complexity: O(n)
    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
  
    #INSERT: Insert a new node at a specific index
    #Time Complexity: O(n)
    def insert(self,index,value):
        #Check if the index is out of range
        if index < 0 or index >= self.length:
            return False
        #Check if the index is the first node
        if index == 0:
            return self.prepend(value)
        #Check if the index is the last node
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        #Get the node before the index
        temp = self.get(index-1)
        #Insert the new node
        new_node.next = temp.next
        #Update the next node
        temp.next = new_node
        #Update the length
        self.length += 1
        return False
        
    #REMOVE: Remove a node at a specific index
    #Time Complexity: O(n)
    def remove(self,index):
        #Check if the index is out of range
        if index < 0 or index >= self.length:
            return None
        #Check if the index is the first node
        if index == 0:
            return self.pop_first()
        #Check if the index is the last node
        if index == self.length - 1:
            return self.pop()
        #Get the node before the index
        prev = self.get(index-1)
        #Get the node at the index
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        #Return the removed node
        return temp

    #REVERSE: Reverse the list
    #Time Complexity: O(n)
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.print_list()
print()
my_linked_list.reverse()
my_linked_list.print_list()