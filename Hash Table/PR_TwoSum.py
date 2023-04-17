"""
HT: Two Sum(⚡Interview Question)

Problem: Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

Input:
A list of integers nums .
A target integer target.

Output:
A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list[].
"""

# Solved in O(n) time and O(n) space, where n is the length of the input array
def two_sum(nums, target):
    # create an empty dictionary
    d = {}

    # loop through the array
    for i in range(len(nums)):
        # find the complement of the current number
        complement = abs(target-nums[i])
        # if the complement is in the dictionary, return the indices of the complement and the current number
        if complement in d:
            return sorted([d[complement], i])
        # else, add the current number to the dictionary
        d[nums[i]] = i
    # if no two numbers add up to the target, return an empty list
    return []


"""
SOLUTION EXPLAINED:
The two_sum function takes an array of integers nums and a target integer target as input, and finds two numbers in the array that add up to the target using a hash table. Here's an explanation of how the function works:
The function creates an empty hash table called num_map to store the numbers in the input array and their indices.
The function loops through each number in the input array nums and uses the enumerate function to get the index of each number. For each number, it calculates the complement of the number by subtracting it from the target.
The function checks if the complement is already in the hash table num_map. If it is, the function returns the indices of the two numbers that add up to the target. The indices are stored in a list [num_map[complement], i] where num_map[complement] is the index of the complement of the current number, and i is the index of the current number.
If the complement is not in the hash table num_map, the function adds the current number and its index to the hash table. This is done by setting num_map[num] = i, where num is the current number and i is its index.
After the loop finishes, the function returns an empty list []. This is because no two numbers in the input array add up to the target.
It has a time complexity of O(n), where n is the length of the input array, because the hash table operations take constant time. This is more efficient than a brute-force solution that checks all pairs of numbers in the array, which would have a time complexity of O(n^2).

"""

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))


"""
    EXPECTED OUTPUT:
    ----------------
    [0, 1]
    [1, 2]
    [0, 1]
    []
    [2, 3]
    [0, 1]
    []

"""
