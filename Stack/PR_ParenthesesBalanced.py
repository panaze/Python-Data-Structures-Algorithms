"""
Stack: Parentheses Balanced (⚡Interview Question)
Check to see if a string of parentheses is balanced or not.
By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order.
For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. 
On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  
Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.
Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.
Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.

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


def is_balanced_parentheses(parentheses):
    # Create a new stack
    stack = Stack()

    # Iterate over each character in the string
    for p in parentheses:
        # If the character is an opening parenthesis,
        # push it onto the stack
        if p == '(':
            stack.push(p)
        # If the character is a closing parenthesis,
        # pop the top element off the stack
        # and check if it matches the opening parenthesis
        elif p == ')':
            # If the stack is empty or the top element
            # is not an opening parenthesis,
            # the parentheses are not balanced
            if stack.is_empty() or stack.pop() != '(':
                return False

    # If the stack is empty, the parentheses are balanced
    return stack.is_empty()


"""
SOLUTION
The function creates a new stack using the Stack() class, and then iterates through each character in the input string using a for loop.
For each character, the function checks if it is an opening parenthesis, represented by the ( character. 
If it is an opening parenthesis, the function pushes it onto the stack using the push method of the stack.
If the character is a closing parenthesis, represented by the ) character, the function checks if the stack is empty or if the top of the stack, which is the most recent opening parenthesis that has not been closed, is not an opening parenthesis. 
If either of these conditions is true, the function returns False because the parentheses are not balanced.
If the top of the stack is an opening parenthesis, the function pops it from the stack using the pop method of the stack. 
The function continues iterating through the input string until all characters have been processed.
After processing all the characters, the function returns True if the stack is empty, which indicates that all opening parentheses have been matched with a closing parenthesis, and False otherwise.
"""


balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

print(is_balanced_parentheses(balanced_parentheses))

print(is_balanced_parentheses(unbalanced_parentheses))


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""
