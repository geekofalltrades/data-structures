import unittest
from data_structures.hash_table import HashTable


class TestGet(unittest.TestCase):
    """Test the get function of the hash (retrieves values based on their
    key).
    """

    def setUp(self):
        self.absent_key = 'NoVal'
        self.pairs = {'aab': 14, 'aVal': 'blargh', 'nutherVal': 3.14}
        self.colliding_pair = ('aba', 'iCollide')
        self.present_pair = ('aab', 14)

    def test_get_from_hash_containing_value(self):
        """Get a value from a hash using a key which it contains."""
        h = HashTable()
        for key, val in self.pairs.items():
            h.set(key, val)
        self.assertEqual(self.present_pair[1], h.get(self.present_pair[0]))

    def test_get_from_hash_not_containing_value(self):
        """Get a value from a hash using a key that it does not contain."""
        h = HashTable()
        self.assertRaises(KeyError, h.get, self.absent_key)

    def test_get_from_hash_with_collisions(self):
        """Get a value from a hash using a key that collides with another
        key in the hash.
        """
        h = HashTable()
        for key, val in self.pairs.items():
            h.set(key, val)
        h.set(self.colliding_pair[0], self.colliding_pair[1])
        self.assertEqual(self.present_pair[1], h.get(self.present_pair[0]))
        self.assertEqual(self.colliding_pair[1], h.get(self.colliding_pair[0]))


class TestSet(unittest.TestCase):
    """Test the set function of the hash (stores a value at the location
    determined by its hashed key).
    """

    def setUp(self):
        self.colliding_pair = ('aba', 'iCollide')
        self.present_pair = ('aab', 14)
        self.overwrite_pair = ('aab', 17)

    def test_set_on_empty_slot(self):
        """Set a value using a key that hashes to an empty bin."""
        h = HashTable()
        h.set(self.present_pair[0], self.present_pair[1])
        self.assertEqual(self.present_pair[1], h.get(self.present_pair[0]))

    def test_set_on_slot_with_collisions(self):
        """Set a value using a key that hashes to a bin already containing
        other keys.
        """
        h = HashTable()
        h.set(self.present_pair[0], self.present_pair[1])
        h.set(self.colliding_pair[0], self.colliding_pair[1])
        self.assertEqual(self.present_pair[1], h.get(self.present_pair[0]))
        self.assertEqual(self.colliding_pair[1], h.get(self.colliding_pair[0]))

    def test_set_on_existing_key(self):
        """Set a value using a key that already exists."""
        h = HashTable()
        h.set(self.present_pair[0], self.present_pair[1])
        self.assertEqual(self.present_pair[1], h.get(self.present_pair[0]))
        h.set(self.overwrite_pair[0], self.overwrite_pair[1])
        self.assertEqual(self.overwrite_pair[1], h.get(self.overwrite_pair[0]))


class TestHash(unittest.TestCase):
    """Test the hash function of the hash (transform a key into a location
    in the hash's storage).
    """

    def setUp(self):
        self.invalid_key = 14
        self.valid_key = 'bob'

    def test_hash_on_invalid_key(self):
        """Try to hash an invalid key (not a string)."""
        h = HashTable()
        self.assertRaises(TypeError, h.hash, self.invalid_key)

    def test_hash_on_valid_key(self):
        """Verify that a string key hashes to the expected value. Somewhat
        tautological.
        """
        h = HashTable()
        hashed = h.hash(self.valid_key)
        expected = sum([ord(i) for i in list(self.valid_key)]) % 16
        self.assertEqual(hashed, expected)


if __name__ == '__main__':
    unittest.main()