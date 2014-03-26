import random
from queue import Queue


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

            self.rebalance(parent)

    def contains(self, val):
        """Test whether the binary search tree contains a given value."""
        if not self.head:
            return False

        if self.head.place(val).value == val:
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

    def in_order(self):
        """An in-order depth-first traversal of the binary search tree."""
        return self.head.in_order()

    def pre_order(self):
        """A pre-order depth-first traversal of the binary search tree."""
        return self.head.pre_order()

    def post_order(self):
        """A post-order depth-first traversal of the binary search tree."""
        return self.head.post_order()

    def breadth_first(self):
        """A breadth-first traversal of the binary search tree."""
        nodes = Queue()
        if self.head:
            nodes.queue(self.head)

        while(nodes.size()):
            node = nodes.dequeue()
            if node.left:
                nodes.queue(node.left)
            if node.right:
                nodes.queue(node.right)

            yield node.value

    def delete(self, val):
        """Remove the node with the given value from the binary search
        tree.
        """
        if not self.head:
            return None

        node = self.head.place(val)
        if node.value != val:
            return None

        if not node.left and not node.right:
            if node is self.head:
                self.head = None
            elif val < node.parent.value:
                node.parent.left = None
            else:
                node.parent.right = None

        elif not node.left:
            if node is self.head:
                self.head = node.right
                self.head.parent = None
            elif val < node.parent.value:
                node.parent.left = node.right
            else:
                node.parent.right = node.right

        elif not node.right:
            if node is self.head:
                self.head = node.left
                self.head.parent = None
            elif val < node.parent.value:
                node.parent.left = node.left
            else:
                node.parent.right = node.left

        else:
            if node.right.depth() >= node.left.depth():
                new = node.right
                if new.left:
                    while new.left:
                        new = new.left
            else:
                new = node.left
                if new.right:
                    while new.right:
                        new = new.right

            new = self.delete(new.value)
            new.right = node.right
            new.left = node.left

            if node is self.head:
                self.head = new
            elif val < node.parent.value:
                node.parent.left = new
            else:
                node.parent.right = new

        if node.parent:
            self.rebalance(node.parent)

        return node

    def rebalance(self, node):
        """Rebalance the tree about the given node."""

        #import pdb; pdb.set_trace()

        #If the tree is skewed to the left.
        if node.balance() < -1:
            #If we have the left-right case, perform a left rotation of
            #the right child of this node's left child.
            if node.left.balance() > 0:
                self._left_rotation(node.left.right)
            #We are now guaranteed to have the left-left case. Perform a
            #right rotation of this node's left child.
            self._right_rotation(node.left)

        #If the tree is skewed to the right.
        elif node.balance() > 1:
            #If we have the right-left case, perform a right rotation of
            #the left child of this node's right child.
            if node.right.balance() < 0:
                self._right_rotation(node.right.left)
            #We are now guaranteed to have the right-right case. Perform
            #a left rotation of this node's right child.
            self._left_rotation(node.right)

        #If this node has become the head of the tree, unset its parent.
        if node is self.head:
            node.parent = None

        #Recurse until the entire tree has been rebalanced.
        if node.parent:
            self.rebalance(node.parent)

    def _right_rotation(self, node):
        """Perform a right rotation of this node with its parent. Assumes
        that the incoming node always has a parent (is not the head of
        the tree).
        """
        parent = node.parent
        child = node.right
        if parent is self.head:
            self.head, node.right, parent.left = \
                node, parent, child
        elif parent is parent.parent.left:
            parent.parent.left, node.right, parent.left = \
                node, parent, child
        else:
            parent.parent.right, node.right, parent.left = \
                node, parent, child

    def _left_rotation(self, node):
        """Perform a left rotation of this node with its parent. Assumes
        that the incoming node always has a parent (is not the head of
        the tree).
        """
        parent = node.parent
        child = node.left
        if parent is self.head:
            self.head, node.left, parent.right = \
                node, parent, child
        elif parent is parent.parent.left:
            parent.parent.left, node.left, parent.right = \
                node, parent, child
        else:
            parent.parent.right, node.left, parent.right = \
                node, parent, child


class BSTNode(object):
    """A node in a binary search tree."""

    def __init__(self, value=None):
        self.value = value
        self._left = None
        self._right = None
        self.parent = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value
        if self._left is not None:
            self._left.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
        if self._right is not None:
            self._right.parent = self

    def place(self, val):
        """Recursively determine the position in the subtree beneath this
        node where a given value lies or should lie.
        """
        if val < self.value:
            return self if not self.left else self.left.place(val)
        elif val > self.value:
            return self if not self.right else self.right.place(val)
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

    def balance(self):
        """Get the balance the subtree rooted at this node. Positive value
        for a right-heavy tree, a negative value for a left-heavy tree. An
        ideally balanced tree has a balance of 0.
        """
        if not self.right and not self.left:
            return 0
        elif not self.right:
            return -self.depth()
        elif not self.left:
            return self.depth()
        else:
            return self.right.depth() - self.left.depth()

    def in_order(self):
        """An in-order depth-first traversal of the subtree beneath this
        node.
        """
        left = self.left.in_order() if self.left else []
        right = self.right.in_order() if self.right else []
        for i in left:
            yield i
        yield self.value
        for i in right:
            yield i

    def pre_order(self):
        """A pre-order depth-first traversal of the subtree beneath this
        node.
        """
        left = self.left.pre_order() if self.left else []
        right = self.right.pre_order() if self.right else []
        yield self.value
        for i in left:
            yield i
        for i in right:
            yield i

    def post_order(self):
        """A post-order depth-first traversal of the subtree beneath this
        node.
        """
        left = self.left.post_order() if self.left else []
        right = self.right.post_order() if self.right else []
        for i in left:
            yield i
        for i in right:
            yield i
        yield self.value

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


def balanced_generator(val):
    num = val
    while num / 2 >= 1:
        div = num / 2
        ret = 0
        while ret < val:
            ret += div
            if ret % num:
                yield ret
        num /= 2


if __name__ == '__main__':
    from time import time

    print """
This tree balances poorly. Inserting 512 sequential values as a
demonstration."""

    b = BST()
    for i in range(512):
        b.insert(i)

    avg = 0
    for i in range(100):
        start = time()
        b.contains(511)
        stop = time()
        avg += (stop - start) / 100

    print """
Finding the last value in the tree took %s seconds
(average of 100 attempts).""" % avg

    print """
Now inserting 512 values in an order which naturally balances the tree."""

    b = BST()

    for i in balanced_generator(512):
        b.insert(i)

    avg = 0
    for i in range(100):
        start = time()
        b.contains(511)
        stop = time()
        avg += (stop - start) / 100

    print """
Finding the last value in the tree took %s seconds
(average of 100 attempts).""" % avg
