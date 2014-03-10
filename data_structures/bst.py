import random

class BST(object):
    """A binary search tree."""

    def __init__(self):
        self.head = None

    def insert(self, val):
        """Insert a value into the binary search tree."""
        if not self.head:
            self.head = BSTNode(val)
        else:
            parent = self.head.place(val)
            if val < parent.value:
                parent.left = BSTNode(val)
            elif val > parent.value:
                parent.right = BSTNode(val)

    def contains(self, val):
        """Test whether the binary search tree contains a given value."""
        if not self.head:
            return False

        node = self.head.place(val)

        if node.value == val:
            return True
        else:
            return False

    def size(self):
        """Get the number of items in the binary search tree."""
        if self.head is None:
            return 0
        else:
            return self.head.size() + 1

    def depth(self):
        """Get the depth of the binary search tree."""
        if self.head is None:
            return 0
        else:
            return self.head.depth() + 1

    def balance(self):
        """Get the balance of the binary search tree. Positive value for
        a right-heavy tree, a negative value for a left-heavy tree. An
        ideally balanced tree has a balance of 0.
        """
        if not self.head or \
                not self.head.right and not self.head.left:
            return 0
        elif not self.head.right:
            return -self.head.depth()
        elif not self.head.left:
            return self.head.depth()
        else:
            return self.head.right.depth() - self.head.left.depth()


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
        if val < self.value and not self.left:
            return self
        elif val < self.value:
            return self.left.place(val)
        elif val > self.value and not self.right:
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

        if self.right:
            ct += self.right.size() + 1

        if self.left:
            ct += self.left.size() + 1

        return ct

    def depth(self):
        """Recursively determine the depth of the deepest subtree beneath
        this node.
        """
        if not self.right and self.left:
            return self.left.depth() + 1
        elif not self.left and self.right:
            return self.right.depth() + 1
        elif not self.left and not self.right:
            return 0
        else:
            return max(self.right.depth(), self.left.depth()) + 1

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.value is None else (
            "\t%s;\n%s\n" % (
                self.value,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
