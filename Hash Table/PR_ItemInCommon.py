"""
HT: Item In Common (⚡Interview Question)
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexit

"""


def item_in_common(list1, list2):
    # create a dictionary
    d = {}

    # loop through the first list and add each item to the dictionary
    for i in range(len(list1)):
        d[i] = True

    # loop through the second list and check if the item is in the dictionary
    for i in range(len(list2)):
        # if the item is in the dictionary, return True
        if list2[i] in d:
            return True

    # if any of the items in the second list are not in the dictionary, return False
    return False


"""
SOLUTION

The function uses a dictionary, my_dict, to store the elements from the first list.

It then loops through the second list, checking if each element is in my_dict.

If an element is found in my_dict, it means that it exists in both lists, so the function returns True.

If no elements are found in common, the function returns False.

"""

list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))


"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
