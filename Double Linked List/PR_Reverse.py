"""
DLL: Reverse (⚡Interview Question)
Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.
To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction. 
Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # Solution solved in O(n)
    def reverse(self):
        current = self.head

        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        self.head, self.tail = self.tail, self.head


"""
SOLUTION
This code is for reversing a doubly linked list by swapping the prev and next pointers of each node.
The method starts by creating a variable temp and setting it to the head of the list. 
We use this variable to traverse the list and perform the swap operation on each node.
Inside the while loop, we swap the prev and next pointers of the current node by using Python's tuple packing and unpacking syntax. We assign the value of temp.next to temp.prev and the value of temp.prev to temp.next, effectively swapping the two pointers.
We then update the value of temp to be the previous node (which is now the next node in the original list). 
We do this by setting temp to temp.prev.
We repeat this process until we have traversed the entire list (i.e., temp is None), at which point we have effectively reversed the list.
Finally, we swap the head and tail pointers of the list by using tuple packing and unpacking. 
We assign the value of self.tail to self.head and the value of self.head to self.tail, effectively reversing the order of the pointers at the beginning and end of the list.
"""


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

"""
