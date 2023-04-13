"""
DLL: Swap Nodes in Pairs (⚡Interview Question)
You are given a doubly linked list.
Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list.
The method should not take any input parameters.

Example:
1-->2-->3-->4--> should become 2-->1-->4-->3-->

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.
Note: You must solve the problem without modifying the values in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)

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

    # Solved in O(n)
    def swap_pairs(self):
        # Create dummy node as a placeholder
        dummy = Node(0)
        # Connect dummy node to head
        dummy.next = self.head
        # Set prev as the dummy node
        prev = dummy

        # Iterate through the list while a pair exists
        while self.head and self.head.next:
            # Assign first and second nodes of the pair
            first_node = self.head
            second_node = self.head.next

            # Swap the pair by updating pointers
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Update prev pointers for swapped nodes
            second_node.prev = prev
            first_node.prev = second_node
            # Update prev pointer of the next node
            if first_node.next:
                first_node.next.prev = first_node

            # Move head to the next pair
            self.head = first_node.next
            # Update prev to the last node in the pair
            prev = first_node

        # Update the head to the new start
        self.head = dummy.next


"""
SOLUTION
This code defines a swap_pairs method that swaps adjacent pairs of nodes in a doubly-linked list. 
The method iterates through the list and swaps each adjacent pair of nodes by updating their next and prev pointers. 
Here's a step-by-step explanation:
1. Create a dummy node with value 0. This dummy node is a placeholder and is used to simplify the head pointer manipulation.
2. Set the next pointer of the dummy node to the current head of the list.
3. Create a prev variable to keep track of the previous node, initially set to the dummy node.
4. Start a while loop that continues as long as the current head and its next node are not None (i.e., there's a pair to swap).
  a. Assign first_node to the current head and second_node to the next node in the list. These are the two nodes that will be swapped.
  b. Update the next pointer of the prev node to point to the second node, effectively placing the second node before the first node in the list.
  c. Update the next pointer of the first node to point to the node after the second node, maintaining the correct order after the swap.
  d. Update the next pointer of the second node to point to the first node, completing the swap.
  e. Update the prev pointers of the swapped nodes to maintain the doubly-linked list structure. Set the prev pointer of the second node to the previous node (before the first node), and the prev pointer of the first node to the second node.
  f. If there's a node after the first node (i.e., first_node.next is not None), update its prev pointer to point back to the first node, maintaining the doubly-linked list structure.
  g. Move the head pointer to the next pair by setting it to the next node of the first node (which is now the second node in the next pair).
  h. Update the prev variable to the first node (which was just swapped), so it's ready for the next iteration.
After the loop, update the head of the list to the next pointer of the dummy node. Since the dummy node was used to simplify head pointer manipulation, the actual head of the list is now the next node after the dummy node.
"""

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs()


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1
    2
    3
    4
    my_dll after swap_pairs:
    2
    1
    4
    3

"""
