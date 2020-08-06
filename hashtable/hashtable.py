class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def get(self, key):
#         current = self.head

#         while current is not None:
#             if current.key == key:
#                 return current
#             current = current.next

#         return current

#     def add_to_head(self, key, value):
#         current = self.head
#         while current is not None:
#             if current.key == key:
#                 current.value = value
#                 return
#             current = current.next

#         new_node = HashTableEntry(key, value)
#         new_node.next = self.head
#         self.head = new_node

#     def add_to_tail(self, key, value)
#         current = self.tail
#         while current is not None:
#             if current.key == key:
#                 current.value = value
#                 return
#             current = current.next

#         new_node = HashTableEntry(key, value)
#         new_node.next = self.tail
#         self.tail = new_node

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.new_list = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.new_list)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        num_items = 0
        for i in self.new_list:
            if i:
                current = i
                num_items += 1
                while current.next:
                    num_items += 1
                    current = current.next
        return num_items / len(self.new_list)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
            hash = hash % self.capacity

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # self.new_list[self.hash_index(key)] = value
        new_index = self.hash_index(key)
        current = self.new_list[new_index]

        if current:
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next:
                    current = current.next
                else:
                    current.next = HashTableEntry(key, value)
        else:
            self.new_list[new_index] = HashTableEntry(key, value)
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.new_list[self.hash_index(key)] = None
        new_index = self.hash_index(key)
        current = self.new_list[new_index]

        if current:
            while current:
                if current.key == key:
                    self.new_list[new_index] = current.next
                    if self.capacity > 16:
                        self.resize(self.capacity / 2)
                    return
                elif current.next:
                    current = current.next
                else:
                    return
        else:
            return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # return self.new_list[self.hash_index(key)]
        if self.new_list[self.hash_index(key)]:
            current = self.new_list[self.hash_index(key)]
            while current.next:
                if current.key == key:
                    return current.value
                current = current.next
            if current.key == key:
                return current.value
        return

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_list = self.new_list
        self.new_list = [None] * new_capacity
        self.capacity = new_capacity
        
        for i in old_list:
            if i:
                self.new_list[self.djb2(i.key)] = i
                current = i.next
                while current:
                    self.new_list[self.djb2(current.key)] = current
                    current = current.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
