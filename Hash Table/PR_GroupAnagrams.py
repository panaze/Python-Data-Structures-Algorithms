from collections import Counter

"""
HT: Group Anagrams (⚡Interview Question)
You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.

"""

# SOLUTION solved in O(n * k log k) time and O(n) space, where n is the length of the input array and k is the maximum length of a string in the input array


def group_anagrams(strings):
    g_a = {}

    # for each string in the list
    for s in strings:
        # sort the string and add it to the dictionary
        cannonical = "".join(sorted(s))
        # if the sorted string is already in the dictionary, append the string to the list
        if cannonical in g_a:
            g_a[cannonical].append(s)
        # else, add the sorted string as a key and the string as a value
        else:
            g_a[cannonical] = [s]

    return list(g_a.values())


"""
SOLUTION EXPLAINED:
The group_anagrams function takes an array of strings as input and groups the anagrams together using a hash table (dictionary). Here's an explanation of how the function works:
The function creates an empty hash table called anagram_groups to store the groups of anagrams.
The function loops through each string in the input array and sorts the characters in each string to get its canonical form.  In the context of this code, "canonical" means the standardized or normalized form of a string that can be used to compare it to other strings to see if they are anagrams. The canonical form is used as the key in the hash table.
The value in the hash table is a list of strings.
The function checks if the canonical form of the current string is already in the hash table. If it is, the current string is added to the existing list of anagrams in the hash table. If not, the current string is added to the hash table as a new group of anagrams.
After the loop finishes, the function returns a list of lists containing the groups of anagrams in the input array. The output is obtained by calling the values method on the anagram_groups hash table, which returns a list of the hash table's values.
It has a time complexity of O(n * k log k), where n is the length of the input array and k is the maximum length of a string in the input array.  The time complexity comes from sorting each string in the array, which takes O(k log k) time, and the loop that goes through each string in the array, which takes O(n) time.
"""


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(
    ["listen", "silent", "triangle", "integral", "garden", "ranged"]))


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
