import unittest
from data_structures.stack import Stack, EmptyError


class TestPush(unittest.TestCase):
    """Test the push function of the stack."""
    def setUp(self):
        self.values = ['bob', 'fred', range(3), 3.14]
        self.single_value = 'teststring'

    def test_push_to_empty_stack(self):
        """Push a value to an empty stack."""
        s = Stack()
        self.assertTrue(s.head is None)
        s.push(self.single_value)
        self.assertEqual(s.head.value, self.single_value)
        self.assertTrue(isinstance(s.head.value, type(self.single_value)))

    def test_push_to_populated_stack(self):
        """Push a value to a populated stack."""
        s = Stack()
        self.assertTrue(s.head is None)
        for val in self.values:
            s.push(val)
        self.assertEqual(s.head.value, self.values[-1])
        self.assertTrue(isinstance(s.head.value, type(self.values[-1])))


class TestPop(unittest.TestCase):
    """Test the pop function of the stack."""
    def setUp(self):
        self.values = ['bob', 'fred', range(3), 3.14]
        self.single_value = 'teststring'

    def test_pop_from_empty_stack(self):
        """Pop a value from an empty stack."""
        s = Stack()
        self.assertTrue(s.head is None)
        self.assertRaises(EmptyError, s.pop)

    def test_pop_from_populated_stack(self):
        """Pop a value from a populated stack."""
        s = Stack()
        s.push(self.single_value)
        popped = s.pop()
        self.assertEqual(popped, self.single_value)
        self.assertTrue(isinstance(popped, type(self.single_value)))


if __name__ == '__main__':
    unittest.main()
