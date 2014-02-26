import unittest
from hash_table import HashTable


class TestGet(unittest.TestCase):
    """Test the get function of the hash (retrieves values based on their
    key).
    """

    def setUp(self):
        pass

    def test_get_from_empty_hash(self):
        pass

    def test_get_from_hash_containing_value(self):
        pass

    def test_get_from_hash_not_containing_value(self):
        pass

    def test_get_from_hash_with_collisions(self):
        pass


class TestSet(unittest.TestCase):
    """Test the set function of the hash (stores a value at the location
    determined by its hashed key).
    """

    def setUp(self):
        pass

    def test_set_on_empty_slot(self):
        pass

    def test_set_on_slot_with_collisions(self):
        pass


class TestHash(unittest.TestCase):
    """Test the hash function of the hash (transform a key into a location
    in the hash's storage).
    """

    def setUp(self):
        pass

    def test_hash_on_invalid_key(self):
        pass

    def test_hash_on_valid_key(self):
        pass


if __name__ == '__main__':
    unittest.main()