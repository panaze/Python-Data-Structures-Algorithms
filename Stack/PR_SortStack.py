"""
Stack: Sort Stack (⚡Interview Question)
The sort_stack function takes a single argument, a Stack object.  
The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack.  
The function should use the pop, push, peek, and is_empty methods of the Stack object.

Note: This is a new function, not a method within the Stack class.


"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

# Solved in O(n^2)


def sort_stack(stack):
    # Create a new stack to hold the sorted elements
    additional_stack = Stack()

    # While the original stack is not empty
    while not stack.is_empty():
        # Remove the top element from the original stack
        temp = stack.pop()

        # While the additional stack is not empty and
        # the top element is greater than the current element
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            # Move the top element from the additional stack to the original stack
            stack.push(additional_stack.pop())

        # Add the current element to the additional stack
        additional_stack.push(temp)

    # Copy the sorted elements from the additional stack to the original stack
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())


"""
SOLUTION
The sort_stack function sorts a given stack of integers in ascending order using only one additional stack. Here's how it works:
First, the function creates a new stack called additional_stack to hold the sorted elements.
Next, the function enters a while loop that continues until the original stack is empty. Inside the loop, the function removes the top element from the original stack using the pop method and stores it in a temporary variable called temp.
The function then enters another while loop that continues until the additional_stack is empty or the top element of additional_stack is less than or equal to temp. Inside the loop, the function removes the top element from the additional_stack using the pop method and adds it back to the original stack using the push method.
Once the inner while loop is exited, the function adds the temp variable to the additional_stack using the push method. This ensures that the additional_stack is always sorted in ascending order.
Once the outer while loop is exited, the function enters another while loop that continues until the additional_stack is empty. Inside the loop, the function removes the top element from the additional_stack using the pop method and adds it back to the original stack using the push method. This step ensures that the original stack is sorted in ascending order.
Finally, the function returns the sorted stack.
Overall, this implementation has a time complexity of O(n^2), where n is the number of elements in the original stack, because the function performs nested loops to compare all the elements with each other. However, it has the advantage of using only one additional stack, which could be useful in certain situations where memory is limited.
"""


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
