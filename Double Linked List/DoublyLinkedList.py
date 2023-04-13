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

    # APPEND: add a node to the end of the list
    # Time Complexity: O(1)
    def append(self, value):
        new_node = Node(value)
        # if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # POP: remove a node from the end of the list
    # Time Complexity: O(1)
    def pop(self):
        # if the list is empty
        if self.head is None:
            return None
        temp = self.tail
        # if the list has only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    # PREPEND: add a node to the beginning of the list
    # Time Complexity: O(1)
    def preapend(self, value):
        new_node = Node(value)
        # if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # POP_FIRST: remove a node from the beginning of the list
    # Time Complexity: O(1)
    def pop_first(self):
        # if the list is empty
        if self.head is None:
            return None
        temp = self.head
        # if the list has only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    # GET: get a node at a specific index
    # Time Complexity: O(n), it is slightly better optimized than singly linked list but still O(n)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # if index is less than half of the length of the list
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        # if index is greater than half of the length of the list
        else:
            temp = self.head
            for _ in range(self.length - 1, index, -1):
                tempr = temp.prev
        return temp

    # SET: set a value of a node at a specific index
    # Time Complexity: O(n)
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # INSERT: insert a node at a specific index
    # Time Complexity: O(n)
    def insert(self, index, value):
        # if index is out of range
        if index < 0 or index > self.length:
            return False
        # if index is 0
        if index == 0:
            # Since prepend is O(1), we can use it and it returns boolean
            return self.preapend(value)
        # if index one more than the last index
        if index == self.length:
            # Since append is O(1), we can use it and it returns boolean
            return self.append(value)

        # if index is somewhere in the middle
        new_node = Node(value)
        # get is O(n) so that is why our general time complexity is O(n)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    # REMOVE: remove a node at a specific index
    # Time Complexity: O(n)
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before

        temp.prev = None
        temp.next = None

        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print(my_doubly_linked_list.remove(1).value, '\n')

my_doubly_linked_list.print_list()
