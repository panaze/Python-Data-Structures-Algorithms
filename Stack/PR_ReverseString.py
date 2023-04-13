"""
Stack: Reverse String (⚡Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.

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


# Solution solved in O(n)
def reverse_string(my_string):
    # create a new stack
    stack = Stack()
    # create an empty string to store the reversed string
    new_string = ""

    # push each character in the string onto the stack
    for char in my_string:
        stack.push(char)

    # pop each character off the stack and apend it to the new string
    for _ in my_string:
        new_string = new_string + stack.pop()

    # return the new string
    return new_string


"""
SOLUTION:
The reverse_string() function uses a stack to reverse a string. 
The string is iterated over, and each character is added to the stack. 
After the stack is filled with all of the characters from the string, the stack is emptied and each character is added to the reversed_string variable. This creates a new string that is the reverse of the original.
This approach works by using the Last-In-First-Out (LIFO) property of a stack. 
The first character in the string is the last character to be added to the stack, and the last character in the string is the first character to be removed from the stack. 
Therefore, reversing the order of the characters is simply a matter of pushing them onto the stack in the opposite order and then popping them off again in that order.

"""

my_string = 'hello'

print(reverse_string(my_string))


"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
