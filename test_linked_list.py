from linked_list import LinkedList
import unittest


class TestInsertFunction(unittest.TestCase):
    def setUp(self):
        self.insert_string = 'bob'
        self.insert_int = 14
        self.insert_float = 3.14

    def test_insert_str_into_empty(self):
        """Insert into a LinkedList that is empty."""
        ll = LinkedList()

        self.assertTrue(ll.head is None)
        ll.insert(self.insert_string)
        self.assertEqual(ll.head.value, self.insert_string)
        self.assertTrue(isinstance(ll.head.value, str))
        self.assertTrue(ll.head.next is None)

    def test_insert_int_into_empty(self):
        """Insert into a LinkedList that is empty."""
        ll = LinkedList()

        self.assertTrue(ll.head is None)
        ll.insert(self.insert_int)
        self.assertEqual(ll.head.value, self.insert_int)
        self.assertTrue(isinstance(ll.head.value, int))
        self.assertTrue(ll.head.next is None)

    def test_insert_float_into_empty(self):
        """Insert into a LinkedList that is empty."""
        ll = LinkedList()

        self.assertTrue(ll.head is None)
        ll.insert(self.insert_float)
        self.assertEqual(ll.head.value, self.insert_float)
        self.assertTrue(isinstance(ll.head.value, float))
        self.assertTrue(ll.head.next is None)

    def test_insert_str_into_populated(self):
        """Insert into a LinkedList that is already populated with some
        values
        """
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        self.assertEqual(ll.head.value, self.insert_string)
        ll.insert(self.insert_string)
        self.assertEqual(ll.head.value, self.insert_string)
        self.assertTrue(isinstance(ll.head.value, str))
        self.assertEqual(ll.head.next.value, self.insert_string)

    def test_insert_int_into_populated(self):
        """Insert into a LinkedList that is already populated with some
        values
        """
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        self.assertEqual(ll.head.value, self.insert_string)
        ll.insert(self.insert_int)
        self.assertEqual(ll.head.value, self.insert_int)
        self.assertTrue(isinstance(ll.head.value, int))
        self.assertEqual(ll.head.next.value, self.insert_string)

    def test_insert_float_into_populated(self):
        """Insert into a LinkedList that is already populated with some
        values
        """
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        self.assertEqual(ll.head.value, self.insert_string)
        ll.insert(self.insert_float)
        self.assertEqual(ll.head.value, self.insert_float)
        self.assertTrue(isinstance(ll.head.value, float))
        self.assertEqual(ll.head.next.value, self.insert_string)


if __name__ == '__main__':
    unittest.main()
