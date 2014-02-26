from linked_list import LinkedList


class HashTable(object):
    """A very naive hast table. Hashes keys (only strings allowed) by the
    summed ordinal value of their characters, and prevents collisions by
    binning any hashed values that collide.
    """

    def __init__(self, size=16):
        """Initialize the hash with the specified number of nodes in its
        internal LinkedList container.
        """
        self.size = size
        self.storage = LinkedList()
        for i in range(size):
            self.storage.insert(LinkedList())

    def get(self, key):
        """Get the value at the specified key, if it exists."""
        bucketNo = self.hash(key)
        bucket = self.storage.head
        for i in range(1, bucketNo):
            bucket = bucket.next

        slot = bucket.value.head
        while(slot):
            if slot.value[0] == key:
                return slot.value[1]
            slot = slot.next

        raise KeyError("No value corresponding to key %s." % key)

    def set(self, key, val):
        """Set the value at the specified key to val, creating it if it
        doesn't exist.
        """
        bucketNo = self.hash(key)
        bucket = self.storage.head
        for i in range(1, bucketNo):
            bucket = bucket.next

        slot = bucket.value.head
        while(slot):
            if slot.value[0] == key:
                slot.value = (key, val)
                return
            slot = slot.next

        bucket.value.insert((key, val))

    def hash(self, key):
        """Hash a key, getting out the corresponding bucket number."""
        if not isinstance(key, str):
            raise ValueError("Attempted to hash a non-string value.")
        return sum([ord(i) for i in list(key)]) % self.size
