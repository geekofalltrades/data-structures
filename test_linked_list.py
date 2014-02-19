from linked_list import LinkedList, LinkedListNode
import unittest


class TestInsertFunction(unittest.TestCase):
    """Test the LinkedList's insert method."""
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


class TestPopFunction(unittest.TestCase):
    """Test the LinkedList's pop method."""
    def setUp(self):
        self.insert_string = 'bob'
        self.insert_int = 14
        self.insert_float = 3.14

    def test_pop_from_empty_list(self):
        """Pop from a LinkedList that is empty."""
        ll = LinkedList()
        self.assertTrue(ll.head is None)
        node = ll.pop()
        self.assertTrue(node is None)
        self.assertTrue(ll.head is None)

    def test_pop_from_one_list(self):
        """Pop from a LinkedList with one node."""
        ll = LinkedList()
        ll.insert(self.insert_string)
        self.assertEqual(ll.head.value, self.insert_string)
        node = ll.pop()
        self.assertEqual(node.value, self.insert_string)
        self.assertTrue(ll.head is None)

    def test_pop_from_many_list(self):
        """Pop from a LinkedList with many nodes."""
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        self.assertEqual(ll.head.value, self.insert_string)
        node = ll.pop()
        self.assertEqual(node.value, self.insert_string)
        self.assertEqual(ll.head.value, self.insert_int)


class TestSizeFunction(unittest.TestCase):
    """Test the LinkedList's size method."""
    def setUp(self):
        self.insert_string = 'bob'
        self.insert_int = 14
        self.insert_float = 3.14

    def test_size_of_empty_list(self):
        """Get the size of an empty LinkedList."""
        ll = LinkedList()
        self.assertTrue(ll.head is None)
        self.assertEqual(ll.size(), 0)

    def test_size_of_populated_list(self):
        """Get the size of a populated LinkedList."""
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        self.assertEqual(ll.head.value, self.insert_string)
        self.assertEqual(ll.size(), 3)


class TestSearchFunction(unittest.TestCase):
    """Test the LinkedList's search method."""
    def setUp(self):
        self.insert_string = 'bob'
        self.insert_int = 14
        self.insert_float = 3.14
        self.value_not_in_list = 'frank'

    def test_search_empty_list(self):
        """Search for a value in an empty LinkedList."""
        ll = LinkedList()

        node = ll.search(self.insert_string)
        self.assertTrue(node is None)

    def test_search_list_without_value(self):
        """Search a populated LinkedList for a value it doesn't contain."""
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        node = ll.search(self.value_not_in_list)
        self.assertTrue(node is None)

    def test_search_list_with_value_at_head(self):
        """Search a populated LinkedList for a value it contains at its head."""
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        node = ll.search(self.insert_string)
        self.assertTrue(isinstance(node, LinkedListNode))
        self.assertEqual(node.value, self.insert_string)

    def test_search_list_with_value_in_middle(self):
        """Search a populated LinkedList for a value it contains in its middle."""
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        node = ll.search(self.insert_int)
        self.assertTrue(isinstance(node, LinkedListNode))
        self.assertEqual(node.value, self.insert_int)

    def test_search_list_with_value_at_tail(self):
        """Search a populated LinkedList for a value it contains at its tail."""
        ll = LinkedList()
        ll.insert(self.insert_float)
        ll.insert(self.insert_int)
        ll.insert(self.insert_string)

        node = ll.search(self.insert_float)
        self.assertTrue(isinstance(node, LinkedListNode))
        self.assertEqual(node.value, self.insert_float)


class TestRemoveFunction(unittest.TestCase):
    """Test the LinkedList's remove method."""
    def setUp(self):
        pass

    def test_remove_empty_list(self):
        """Remove from an empty LinkedList."""

    def test_remove_list_without_value(self):
        """Remove from a populated LinkedList a value it doesn't contain."""

    def test_remove_list_with_value(self):
        """Remove from a populated LinkedList a value it contains."""


class TestStrFunction(unittest.TestCase):
    """Test the LinkedList's ___str___ method."""
    def setUp(self):
        pass

    def test_str_empty_list(self):
        """Get the string representation of an empty LinkedList."""

    def test_str_one_list(self):
        """Get the string representation of a LinkedList with one value."""

    def test_str_many_list(self):
        """Get the string representation of a LinkedList with many values."""


if __name__ == '__main__':
    unittest.main()
