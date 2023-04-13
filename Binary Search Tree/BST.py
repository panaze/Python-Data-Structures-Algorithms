class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    # CONSTUCTOR: create a new empty BST
    # Time Complexity: O(1)
    def __init__(self):
        self.root = None

    # INSERT: add a new node to the BST
    # Time Complexity: O(log n)
    def insert(self, value):
        # create a new node
        new_node = Node(value)

        # if the tree is empty, make the new node the root
        if self.root is None:
            self.root = new_node
            return True

        # if the tree is not empty, find the correct place for the new node
        # start at the root
        temp = self.root

        while True:
            # if the new node's value is the same as the current node's value, return False
            if new_node.value == temp.value:
                return False
            # if the new node's value is less than the current node's value we go left
            if new_node.value < temp.value:
                # if the current node has no left child, make the new node the left child
                if temp.left is None:
                    temp.left = new_node
                    return True
                # if the current node has a left child, move to that node and repeat
                temp = temp.left

            # if the new node's value is greater than the current node's value we go right
            else:
                # if the current node has no right child, make the new node the right child
                if temp.right is None:
                    temp.right = new_node
                    return True
                # if the current node has a right child, move to that node and repeat
                temp = temp.right

    # CONTAINS: check if a value is in the BST
    # Time Complexity: O(n)
    def contains(self, value):
        # Get a reference to the root node
        temp = self.root

        # Loop through the tree
        while temp is not None:
            # If the value is less than the current node's value, go left
            if value < temp.value:
                temp = temp.left
            # If the value is greater than the current node's value, go right
            elif value > temp.value:
                temp = temp.right
            # If the value is equal to the current node's value, return True
            else:
                return True

        # If we get here, the value is not in the tree
        return False


my_tree = BST()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.contains(27))
print(my_tree.contains(17))
