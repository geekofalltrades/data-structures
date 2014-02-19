class LinkedList(object):
    """A singly-linked list."""

    def __init__(self):
        self.head = None

    def __str__(self):
        retval = []
        nextnode = self.head
        while nextnode is not None:
            retval.append(nextnode.value)
            nextnode = nextnode.next

        return retval

    def insert(self, item):
        self.head = LinkedListNode(item, self.head)

    def pop(self):
        pass

    def size(self):
        ct = 0
        nextnode = self.head
        while nextnode is not None:
            nextnode = nextnode.next
            ct += 1

        return ct

    def search(self, item):
        nextnode = self.head
        while nextnode is not None:
            if nextnode.value == item:
                return True
        return False

    def remove(self, item):
        pass


class LinkedListNode(object):
    def __init__(self, value=None, nextnode=None):
        self.value = value
        self.next = nextnode


if __name__ == '__main__':
    pass
    #eventually run some demonstration code here?
