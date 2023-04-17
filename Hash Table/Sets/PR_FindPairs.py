
"""
Set: Find Pairs (⚡Interview Question)
You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.

Input
Your function should take in the following inputs:
arr1: a list of integers
arr2: a list of integers
target: an integer

Output
Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.

Example
Here's an example of what your function should return:

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7
 
pairs = find_pairs(arr1, arr2, target)
print (pairs)
# Output: [(5, 2), (3, 4), (1, 6)]


In this example, the pairs (5, 2) , (3, 4) , and (1, 6) are the only pairs of numbers (one from arr1 and one from arr2) whose sum is 7.

"""

# Solved in O(n) time and O(n) space


def find_pairs(arr1, arr2, target):

    a1 = set(arr1)
    pairs = []

    for num in arr2:
        complement = target - num
        if complement in a1:
            pairs.append((complement, num))

    return pairs


"""
SOLUTION:
The find_pairs function takes three arguments: arr1, arr2, and target.

arr1 and arr2 are lists of integers.

The function creates a set called set1 containing all the elements in arr1.

target is also an integer, which represents the target sum that the function is looking for.

The function then initializes an empty list called pairs.

The function then loops through each element in arr2 and for each element, it calculates its complement as complement = target - num.

The function then checks if complement is present in set1 using the in operator.  If it is, then the function has found a pair of numbers that add up to target, and it appends this pair (in the form of a tuple) to the pairs list.

Finally, the function returns the pairs list, which contains all pairs of numbers from arr1 and arr2 that add up to target.


"""

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)


"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
