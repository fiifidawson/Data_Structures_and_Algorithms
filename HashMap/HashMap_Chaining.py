""" 
How to handle collision in HashMap?
    - Separate Chaining
    - Linear Probing
"""

# Hash function
def get_hash(key):

    hash = 0
    for char in key:
        hash += ord(char)# Find the ASCII value of the character and add it to the hash
    return hash % 100 # Mod the hash by the size of the array to get a valid array index


# Hash map class
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] # Create an array of size 100

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX # Mod the hash by the size of the array to get a valid array index
    
    # add() or __setitem__()
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][idx] = (key, val)
                found = True
                break
        if not found:
            #if key does not exist in linked list
            self.arr[hash].append((key, val))
    
    # get() or __getitem__()
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for element in self.arr[arr_index]:
            if element[0] == key: # element[0] is the key
                return element[1] # element[1] is the value
        
    
    # delete() or __delitem__()
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]
        



# Driver code
t = HashTable()
t['march 6'] = 130
t['march 6'] = 90
t['march 8'] = 67
t['march 9'] = 34

print(t.arr)