class HashTable:
    # CONSTUCTOR: creates a list of size 7 with all values set to None
    # TIME COMPLEXITY: O(1)
    def __init__(self, size=7):
        self.data_map = [None] * size

    # HASH FUNCTION: takes a key and returns a hash value
    # the hash value is the address in the data map where the key-value pair will be stored
    # TIME COMPLEXITY: O(1)
    def __hash(self, key):
        my_hash = 0
        # for each letter in the key, add the ASCII value of the letter to the hash times 23 and mod it by the length of the data map
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        # return the hash (address in the data map)
        return my_hash

    # PRINT TABLE: prints the data map
    # TIME COMPLEXITY: O(n)
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    # SET: takes a key and a value and adds the key-value pair to the data map
    # TIME COMPLEXITY: O(1)
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # GET: takes a key and returns the value associated with the key
    # TIME COMPLEXITY: O(1) or O(n) if there is a collision, n is the number of key-value pairs in the bucket
    def get(self, key):
        # get the index of the key
        index = self.__hash(key)

        # if the index is not None, loop through the bucket and return the value associated with the key
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                # if the key is found, return the value
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        # if the key is not found, return None
        return None

    # KEYS: returns a list of all the keys in the data map
    # TIME COMPLEXITY: O(n) or O(n^2) if there is a collision, n is the number of key-value pairs in the bucket
    def keys(self):
        all_keys = []
        # loop through the data map and add all the keys to the list
        for i in range(len(self.data_map)):
            # if the bucket is not None, loop through the bucket and add the keys to the list
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    # add the key to the list
                    all_keys.append(self.data_map[i][j][0])
        # return the list of keys
        return all_keys


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())
