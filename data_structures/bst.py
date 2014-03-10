class BST(object):
    """A binary search tree."""

    def __init__(self):
        self.head = None

    def insert(self, val):
        """Insert a value into the binary search tree."""
        parent = self.head.place(val)
        if val < parent.val:
            parent.left = BSTNode(val)
        elif val > parent.val:
            parent.right = BSTNode(val)

    def contains(self, val):
        """Test whether the binary search tree contains a given value."""
        node = self.head.place(val)

        if node.value == val:
            return True
        else:
            return False

    def size(self):
        """Get the number of items in the binary search tree."""
        pass

    def depth(self):
        """Get the depth of the binary search tree."""
        pass

    def balance(self):
        """Get the balance of the binary search tree. Positive value for
        a right-heavy tree, a negative value for a left-heavy tree. An
        ideally balanced tree has a balance of 0.
        """
        pass


class BSTNode(object):
    """A node in a binary search tree."""

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def place(self, val):
        """Recursively determine the position in the subtree beneath this
        node where a given value lies or should lie.
        """
        if val < self.value and self.left is None:
            return self
        elif val < self.value:
            return self.left.place(val)
        elif val > self.value and self.right is None:
            return self
        elif val > self.value:
            return self.right.place(val)
        else:
            return self

    def size(self):
        """Recursively count the number of nodes that lie beneath this
        node.
        """
        ct = 0

        if self.right is not None:
            ct += self.right.size() + 1

        if self.left is not None:
            ct += self.left.size() + 1

        return ct

    def depth(self):
        """Recursively determine the depth of the deepest subtree beneath
        this node.
        """
        if self.right is None and self.left is not None:
            return self.left.depth() + 1
        elif self.left is None and self.right is not None:
            return self.right.depth() + 1
        elif self.left is None and self.right is None:
            return 0
        else:
            return max(self.right.depth(), self.left.depth()) + 1
