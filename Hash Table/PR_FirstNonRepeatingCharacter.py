from collections import Counter

"""
HT: First Non-Repeating Character (⚡Interview Question)
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.

"""


def first_non_repeating_char(string):

    # Way 1: Using Counter to create a dictionary with the number of times each item appears in the list
    # d = dict(Counter(string))

    # Way 2: Manually
    # create a dictionary
    d = {}

    # loop through the list
    for i in range(len(string)):
        # if the item is in the dictionary, increment the value by 1
        if string[i] in d:
            d[string[i]] = d[string[i]] + 1
        # if the item is not in the dictionary, add it to the dictionary with a value of 1
        else:
            d[string[i]] = 1

    for key in d:
        if d[key] == 1:
            return key

    return None


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
