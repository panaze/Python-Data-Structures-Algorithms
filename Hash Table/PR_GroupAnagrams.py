from collections import Counter

"""
HT: Group Anagrams (⚡Interview Question)
You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.

"""


def group_anagrams(strings):
    finalList = []
    arr_strings = strings

    while len(arr_strings) != 0:
        anagram_List = []
        anagram_List.append(arr_strings[0])

        d = dict(Counter(arr_strings[0]))

        if len(arr_strings) == 1:
            finalList.append(anagram_List)
            break

        for i in range(1, len(arr_strings)):
            d2 = dict(Counter(arr_strings[i]))

            if d == d2:
                del arr_strings[i]
                anagram_List.append(arr_strings[i])

        del arr_strings[0]
        finalList.append(anagram_List)

    return finalList


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
