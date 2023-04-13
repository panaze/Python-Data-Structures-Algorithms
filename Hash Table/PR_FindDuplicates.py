from collections import Counter


"""
HT: Find Duplicates (⚡Interview Question)

Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).

Input:
A list of integers nums.
 
Output:
A list of integers representing the numbers in the input array nums that appear more than once. 
If no duplicates are found in the input array, return an empty list [].

"""


def find_duplicates(nums):
    # create the empty list that will hold the duplicates
    finalList = []

    # Way 1: Using Counter to create a dictionary with the number of times each item appears in the list
    # d = dict(Counter(nums))

    # Way 2: Manually
    # create a dictionary
    d = {}

    # loop through the list
    for i in range(len(nums)):
        # if the item is in the dictionary, increment the value by 1
        if nums[i] in d:
            d[nums[i]] = d[nums[i]] + 1
        # if the item is not in the dictionary, add it to the dictionary with a value of 1
        else:
            d[nums[i]] = 1

    # loop through the dictionary and add the keys to the final list if the value is greater than 1
    for key in d:
        if d[key] > 1:
            finalList.append(key)

    # return the final list
    return finalList


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))


"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
