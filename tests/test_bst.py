import unittest
from data_structures.bst import BST


class TestInsert(unittest.TestCase):
    """Test the insert method of the binary search tree class."""
    def setUp(self):
        self.b = BST()

    def test_insert_into_empty_tree(self):
        """Attempt to insert into an empty tree."""
        self.b.insert(7)
        self.assertTrue(self.b.head is not None)
        self.assertEqual(self.b.head.value, 7)
        self.assertTrue(self.b.head.left is None)
        self.assertTrue(self.b.head.right is None)

    def test_insert_to_left(self):
        """Insert into a tree with a head node a value that should go to
        the left of the head node.
        """
        self.b.insert(7)
        self.b.insert(4)
        self.assertEqual(self.b.head.value, 7)
        self.assertEqual(self.b.head.left.value, 4)
        self.assertTrue(self.b.head.right is None)
        self.assertTrue(self.b.head.left.left is None)
        self.assertTrue(self.b.head.left.right is None)

    def test_insert_to_right(self):
        """Insert into a tree with a head node a value that should go to
        the right of the head node.
        """
        self.b.insert(7)
        self.b.insert(10)
        self.assertEqual(self.b.head.value, 7)
        self.assertEqual(self.b.head.right.value, 10)
        self.assertTrue(self.b.head.left is None)
        self.assertTrue(self.b.head.right.left is None)
        self.assertTrue(self.b.head.right.right is None)


class TestContains(unittest.TestCase):
    """Test the contains method of the binary search tree class."""
    def setUp(self):
        pass

    def test_contains_on_empty_tree(self):
        """Test whether an empty tree contains a given value."""
        pass

    def test_contains_on_head_node(self):
        """Test whether a value at the head node is visible to the
        contains function.
        """
        pass

    def test_contains_on_lower_node(self):
        """Test whether a value below the head node is visible to the
        contains function.
        """
        pass

    def test_contains_on_heavily_populated_tree(self):
        """Test whether a heavily populated tree can find a value inserted
        near its end.
        """
        pass


class TestSize(unittest.TestCase):
    """Test the size method of the binary search tree class."""
    def setUp(self):
        pass

    def test_size_on_empty_tree(self):
        """Test the size of an empty tree."""
        pass

    def test_size_on_populated_tree(self):
        """Test the size of a populated tree."""
        pass


class TestDepth(unittest.TestCase):
    """Test the depth method of the binary search tree class."""
    def setUp(self):
        pass

    def test_depth_on_empty_tree(self):
        """Test the depth of an empty tree."""
        pass

    def test_depth_on_one_level_tree(self):
        """Test the depth of a tree with one level (a head node)."""
        pass

    def test_depth_on_two_level_tree(self):
        """Test the depth of a tree with two levels."""
        pass


class TestBalance(unittest.TestCase):
    """Test the balance method of the binary search tree class."""
    def setUp(self):
        pass

    def test_balance_on_empty_tree(self):
        """Retrieve the balance of an empty tree."""
        pass

    def test_balance_on_head_node(self):
        """Retrieve the balance of a tree with only a head node."""
        pass

    def test_balance_on_right_heavy_tree(self):
        """Retrieve the balance of a tree that is weighted to the right.
        """
        pass

    def test_balance_on_left_heavy_tree(self):
        """Retrieve the balance of a tree that is weighted to the left.
        """
        pass


if __name__ == '__main__':
    unittest.main()
