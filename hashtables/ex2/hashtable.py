class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


myEntry = HashTableEntry('hello', 'world')  # creates an object in memory


print(myEntry.key)
print(myEntry.value)
print(myEntry.next)

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        # Number of buckets in the hash table
        self.capacity = max(capacity, MIN_CAPACITY)
        self.storage = [None] * self.capacity
        # Number of keys in hash table
        self.items_in_hash_table = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        # number of items divided by number of buckets
        # try to keep between 20% and 70%
        # how are these numbers derived? idk,
        # academic testing or real-world testing?
        return self.items_in_hash_table / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """
        hash_value = 0x811c9dc5
        fnv_prime = 0x01000193

        for byte in key.encode('UTF-8', 'ignore'):
            hash_value = (hash_value * fnv_prime)
            hash_value = hash_value ^ byte
        return hash_value

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """
        h_value = 5381
        for char in key:
            h_value = ((h_value << 5) + h_value) + ord(char)
        return h_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        """
        idx = self.hash_index(key)

        # If empty, insert at idx
        if self.storage[idx] is None:
            self.storage[idx] = HashTableEntry(key, value)
            self.items_in_hash_table += 1

            # if load factor exceeds 0.66, resize
            if self.get_load_factor() > 0.66:
                self.resize(self.capacity * 2)
            return

        # If not empty --> if key already exists, overwrite
        while self.storage[idx] is not None:
            if self.storage[idx].key == key:
                self.storage[idx].value = value
                return
            self.storage[idx] = self.storage[idx].next

        # If no key --> put at the beginning of storage
        head = self.storage[idx]
        self.storage[idx] = HashTableEntry(key, value)
        self.storage[idx].next = head
        self.items_in_hash_table += 1

        if self.get_load_factor() > 0.66:
            return self.resize(new_capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        """
        # find the matching pair of values
        # and point the previous node of that one
        # to the next node of the found node
        idx = self.hash_index(key)
        curr = self.storage[idx]

        # If key is in head --> delete
        if curr.key == key:
            self.storage[idx] = self.storage[idx].next
            self.items_in_hash_table -= 1
            return curr.value

        # If not at the head --> check the rest of the storage
        while curr.next is not None:
            if curr.next.key == key:
                curr.next == curr.next.next
                self.items_in_hash_table -= 1
                return curr
        print(f"KeyError: {key} Doesn't exist")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        # hash the key to find the index of the value
        idx = self.hash_index(key)

        while self.storage[idx] is not None:
            if self.storage[idx].key == key:
                return self.storage[idx].value
            self.storage[idx] = self.storage[idx].next
        # return None
        print(f"KeyError: {key} Doesn't exist")

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # resize O(n)
        self.capacity = new_capacity
        old_storage = self.storage
        self.storage = new_capacity * [None]

        for ii in old_storage:
            while ii is not None:
                self.put(ii.key, ii.value)
                ii = ii.next
