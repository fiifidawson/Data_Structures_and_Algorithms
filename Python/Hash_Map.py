class HashMap:
    def __init__(self):
        self.capacity = 16
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def hash(self, key):
        # Simple hash function using the built-in hash function
        return hash(key) % self.capacity

    def put(self, key, value):
        # Check if the load factor is greater than 0.7
        if (self.size / self.capacity) > 0.7:
            self._resize()

        # Get the hash of the key
        hash_key = self.hash(key)

        # Check if the key already exists in the hash map
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                self.buckets[hash_key][i] = (key, value)
                return

        # Add the (key, value) pair to the bucket at the hashed index
        self.buckets[hash_key].append((key, value))
        self.size += 1

    def get(self, key):
        # Get the hash of the key
        hash_key = self.hash(key)

        # Check if the key exists in the hash map
        for k, v in self.buckets[hash_key]:
            if k == key:
                return v

        # If the key is not found, return None
        return None

    def remove(self, key):
        # Get the hash of the key
        hash_key = self.hash(key)

        # Check if the key exists in the hash map
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                del self.buckets[hash_key][i]
                self.size -= 1
                return

    def _resize(self):
        # Double the capacity of the hash map and rehash all the keys
        self.capacity *= 2
        new_buckets = [[] for _ in range(self.capacity)]

        for bucket in self.buckets:
            for k, v in bucket:
                hash_key = self.hash(k)
                new_buckets[hash_key].append((k, v))

        self.buckets = new_buckets
