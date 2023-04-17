
"""
Set: Has Unique Chars (⚡Interview Question)
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.

"""


def has_unique_chars(s):
    s_l = set(list(s))

    if len(s) == len(s_l):
        return True
    else:
        return False


"""
SOLUTION:
For this problem, we can use a set to solve it. A set is an unordered collection of unique items. 
So, if we convert the string to a set, and then compare the length of the set to the length of the string, we can determine if the string has unique characters or not.

"""

print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""
