import unittest
from data_structures.bst import BST, balanced_generator
from random import shuffle


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
        self.b = BST()

    def test_contains_on_empty_tree(self):
        """Test whether an empty tree contains a given value."""
        self.assertEqual(self.b.contains(7), False)

    def test_contains_on_head_node(self):
        """Test whether a value at the head node is visible to the
        contains function.
        """
        self.b.insert(7)
        self.assertEqual(self.b.contains(7), True)

    def test_contains_on_lower_node(self):
        """Test whether a value below the head node is visible to the
        contains function.
        """
        self.b.insert(5)
        self.b.insert(3)
        self.b.insert(22)
        self.b.insert(7)
        self.assertEqual(self.b.contains(7), True)

    def test_contains_on_heavily_populated_tree(self):
        """Test whether a heavily populated tree can find a value inserted
        near its end.
        """
        rand = range(1000)
        shuffle(rand)
        for i in rand:
            self.b.insert(i)

        self.b.insert(1000)
        self.assertEqual(self.b.contains(1000), True)


class TestSize(unittest.TestCase):
    """Test the size method of the binary search tree class."""
    def setUp(self):
        self.b = BST()

    def test_size_on_empty_tree(self):
        """Test the size of an empty tree."""
        self.assertEqual(self.b.size(), 0)

    def test_size_on_populated_tree(self):
        """Test the size of a populated tree."""
        rand = range(1000)
        shuffle(rand)
        for i in rand:
            self.b.insert(i)

        self.assertEqual(self.b.size(), 1000)


class TestDepth(unittest.TestCase):
    """Test the depth method of the binary search tree class."""
    def setUp(self):
        self.b = BST()

    def test_depth_on_empty_tree(self):
        """Test the depth of an empty tree."""
        self.assertEqual(self.b.depth(), 0)

    def test_depth_on_one_level_tree(self):
        """Test the depth of a tree with one level (a head node)."""
        self.b.insert(7)
        self.assertEqual(self.b.depth(), 1)

    def test_depth_on_two_level_tree(self):
        """Test the depth of a tree with two levels."""
        self.b.insert(7)
        self.b.insert(10)
        self.assertEqual(self.b.depth(), 2)


class TestBalance(unittest.TestCase):
    """Test the balance method of the binary search tree class."""
    def setUp(self):
        self.b = BST()

    def test_balance_on_empty_tree(self):
        """Retrieve the balance of an empty tree."""
        self.assertEqual(self.b.balance(), 0)

    def test_balance_on_head_node(self):
        """Retrieve the balance of a tree with only a head node."""
        self.b.insert(7)
        self.assertEqual(self.b.balance(), 0)

    def test_balance_on_right_heavy_tree(self):
        """Retrieve the balance of a tree that is weighted to the right.
        """
        for i in range(10):
            self.b.insert(i)

        self.assertEqual(self.b.balance(), 9)

    def test_balance_on_left_heavy_tree(self):
        """Retrieve the balance of a tree that is weighted to the left.
        """
        for i in range(9, -1, -1):
            self.b.insert(i)

        self.assertEqual(self.b.balance(), -9)


class TestTraversals(unittest.TestCase):
    """Test the four traversal algorithms now incorporated into the tree.
    """
    def setUp(self):
        self.b = BST()
        for i in balanced_generator(8):
            self.b.insert(i)

        self.in_order = [1, 2, 3, 4, 5, 6, 7]
        self.pre_order = [4, 2, 1, 3, 6, 5, 7]
        self.post_order = [1, 3, 2, 5, 7, 6, 4]
        self.breadth_first = [4, 2, 6, 1, 3, 5, 7]

    def test_in_order(self):
        """Test in-order traversal of the tree."""
        self.assertEqual(list(self.b.in_order()), self.in_order)

    def test_pre_order(self):
        """Test pre-order traversal of the tree."""
        self.assertEqual(list(self.b.pre_order()), self.pre_order)

    def test_post_order(self):
        """Test post-order traversal of the tree."""
        self.assertEqual(list(self.b.post_order()), self.post_order)

    def test_breadth_first(self):
        """Test breadth-first traversal of the tree."""
        self.assertEqual(list(self.b.breadth_first()), self.breadth_first)


class TestDelete(unittest.TestCase):
    """Test the delete method of the binary search tree."""
    def setUp(self):
        self.b = BST()
        for i in balanced_generator(8):
            self.b.insert(i)

        self.in_order = [1, 2, 3, 4, 5, 6, 7]
        self.pre_order = [4, 2, 1, 3, 6, 5, 7]
        self.post_order = [1, 3, 2, 5, 7, 6, 4]
        self.breadth_first = [4, 2, 6, 1, 3, 5, 7]

    def test_delete_from_empty_tree(self):
        """Verify that deleting from an empty tree is a no-op."""
        self.b = BST()
        self.assertIsNone(self.b.delete(10))
        self.assertIsNone(self.b.head)

    def test_delete_value_not_in_tree(self):
        """Verify that deleting a value not in the tree is a no-op."""
        start = list(self.b.in_order())
        self.assertIsNone(self.b.delete(10))
        end = list(self.b.in_order())
        self.assertEqual(start, end)

    def test_delete_node_with_no_children(self):
        """Delete a node with no children and assert that the tree assumes
        the expected structure.
        """
        pass

    def test_delete_node_with_right_children(self):
        """Delete a node with only right children and assert that the
        tree assumes the expected structure.
        """
        pass

    def test_delete_node_with_left_children(self):
        """Delete a node with only left children and assert that the
        tree assumes the expected structure.
        """
        pass

    def test_delete_node_with_both_children(self):
        """Delete a node that has left and right children and assert that
        it assumes the expected structure.
        """
        pass

    def test_delete_head_node(self):
        """Delete the nead node and assert that the tree assumes the
        expcected structure.
        """
        pass


if __name__ == '__main__':
    unittest.main()
