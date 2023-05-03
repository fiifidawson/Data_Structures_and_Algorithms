"""Implementing a hash map"""
"""Space complexity: O(n)
   Time complexity: O(1)
"""


# Hash map class
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] # Create an array of size 100

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)# Find the ASCII value of the character and add it to the hash
        return hash % self.MAX # Mod the hash by the size of the array to get a valid array index
    
    # add() or __setitem__()
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        self.arr[hash] = val
    
    # get() or __getitem__()
    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]
    
    # delete() or __delitem__()
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None

# Driver code
t = HashTable()
# One way of doing it
# t.add('march 6', 130)
# t.get('march 6')

# Another way of doing it
t['march 6'] = 130
t['march 6'] 

print(t.arr)